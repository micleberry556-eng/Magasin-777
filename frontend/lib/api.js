/**
 * API client for communicating with the backend.
 * In Docker, requests go through Nginx gateway.
 * In dev, they go directly to the backend.
 */

const API_BASE = typeof window !== "undefined"
  ? ""  // Browser: relative URLs go through Nginx
  : (process.env.INTERNAL_API_URL || "http://evaluator-service:8000");

export async function apiFetch(path, options = {}) {
  const url = `${API_BASE}${path}`;
  const res = await fetch(url, {
    headers: { "Content-Type": "application/json", ...options.headers },
    ...options,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(err.detail || `API error ${res.status}`);
  }
  return res.json();
}

export async function adminFetch(path, token, options = {}) {
  return apiFetch(path, {
    ...options,
    headers: { Authorization: `Bearer ${token}`, ...options.headers },
  });
}
