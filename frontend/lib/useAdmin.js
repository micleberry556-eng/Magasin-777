/**
 * Admin auth context — single shared token across all admin pages.
 */
import { createContext, useContext, useState, useEffect, useCallback, useRef } from "react";

const AdminContext = createContext(null);

export function AdminProvider({ children }) {
  const [token, setTokenState] = useState(null);
  const [loading, setLoading] = useState(true);
  const tokenRef = useRef(null);

  useEffect(() => {
    try {
      const saved = localStorage.getItem("lm_admin_token");
      if (saved) {
        setTokenState(saved);
        tokenRef.current = saved;
      }
    } catch {}
    setLoading(false);
  }, []);

  const setToken = useCallback((t) => {
    setTokenState(t);
    tokenRef.current = t;
  }, []);

  const login = useCallback(async (email, password) => {
    const res = await fetch("/api/admin/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || "Login failed");
    }
    const data = await res.json();
    setToken(data.access_token);
    localStorage.setItem("lm_admin_token", data.access_token);
    return data;
  }, [setToken]);

  const logout = useCallback(() => {
    setToken(null);
    localStorage.removeItem("lm_admin_token");
  }, [setToken]);

  const adminFetch = useCallback(async (path, options = {}) => {
    // Always read from ref to get the latest token, avoiding stale closures
    const currentToken = tokenRef.current;
    if (!currentToken) {
      throw new Error("Not authenticated");
    }
    const res = await fetch(path, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${currentToken}`,
        ...options.headers,
      },
    });
    if (res.status === 401 || res.status === 403) {
      logout();
      throw new Error("Session expired");
    }
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `Error ${res.status}`);
    }
    return res.json();
  }, [logout]);

  return (
    <AdminContext.Provider value={{ token, loading, login, logout, adminFetch }}>
      {children}
    </AdminContext.Provider>
  );
}

export function useAdmin() {
  const ctx = useContext(AdminContext);
  if (!ctx) throw new Error("useAdmin must be used within AdminProvider");
  return ctx;
}
