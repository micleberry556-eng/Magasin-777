/**
 * Admin auth hook — stores JWT token in localStorage.
 */
import { useState, useEffect, useCallback } from "react";

export function useAdmin() {
  const [token, setTokenState] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    try {
      const saved = localStorage.getItem("lm_admin_token");
      if (saved) setTokenState(saved);
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
    setTokenState(data.access_token);
    localStorage.setItem("lm_admin_token", data.access_token);
    return data;
  }, []);

  const logout = useCallback(() => {
    setTokenState(null);
    localStorage.removeItem("lm_admin_token");
  }, []);

  const adminFetch = useCallback(async (path, options = {}) => {
    const res = await fetch(path, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
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
  }, [token, logout]);

  return { token, loading, login, logout, adminFetch };
}
