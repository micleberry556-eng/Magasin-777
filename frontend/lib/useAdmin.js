/**
 * Admin auth context — single shared token across all admin pages.
 * Always mounted in _app.js to survive page transitions.
 */
import { createContext, useContext, useState, useEffect, useCallback, useRef } from "react";

const AdminContext = createContext(null);

export function AdminProvider({ children }) {
  const [token, setTokenState] = useState(null);
  const [loading, setLoading] = useState(true);
  const tokenRef = useRef(null);

  // Read token from localStorage once on mount
  useEffect(() => {
    try {
      const saved = localStorage.getItem("lm_admin_token");
      if (saved) {
        tokenRef.current = saved;
        setTokenState(saved);
      }
    } catch {}
    setLoading(false);
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
    tokenRef.current = data.access_token;
    setTokenState(data.access_token);
    try { localStorage.setItem("lm_admin_token", data.access_token); } catch {}
    return data;
  }, []);

  const logout = useCallback(() => {
    tokenRef.current = null;
    setTokenState(null);
    try { localStorage.removeItem("lm_admin_token"); } catch {}
  }, []);

  // Stable adminFetch — never changes identity, reads token from ref
  const adminFetchRef = useRef(null);
  adminFetchRef.current = async (path, options = {}) => {
    const currentToken = tokenRef.current;
    if (!currentToken) {
      return null; // Not authenticated yet — return null instead of throwing
    }
    const res = await fetch(path, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${currentToken}`,
        ...(options.headers || {}),
      },
    });
    if (res.status === 401) {
      // Token expired — clear it
      tokenRef.current = null;
      setTokenState(null);
      try { localStorage.removeItem("lm_admin_token"); } catch {}
      return null;
    }
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `Error ${res.status}`);
    }
    return res.json();
  };

  // Stable function reference that never changes — prevents useEffect re-runs
  const adminFetch = useCallback(
    (path, options) => adminFetchRef.current(path, options),
    []
  );

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
