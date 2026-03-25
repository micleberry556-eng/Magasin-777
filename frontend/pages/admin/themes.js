/**
 * Admin themes — browse 300 themes, preview, activate.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

function Themes() {
  const { adminFetch } = useAdmin();
  const [themes, setThemes] = useState([]);
  const [categories, setCategories] = useState([]);
  const [activeFilter, setActiveFilter] = useState("");
  const [activeThemeId, setActiveThemeId] = useState(null);
  const [page, setPage] = useState(0);
  const PAGE_SIZE = 50;

  useEffect(() => {
    fetch("/api/themes/categories").then((r) => r.json()).then(setCategories).catch(() => {});
    fetch("/api/settings").then((r) => r.json()).then((s) => setActiveThemeId(s.active_theme_id)).catch(() => {});
  }, []);

  useEffect(() => {
    let url = `/api/themes?skip=${page * PAGE_SIZE}&limit=${PAGE_SIZE}`;
    if (activeFilter) url += `&category=${activeFilter}`;
    fetch(url).then((r) => r.json()).then(setThemes).catch(() => {});
  }, [activeFilter, page]);

  const activate = async (themeId) => {
    try {
      await adminFetch(`/api/admin/themes/${themeId}/activate`, { method: "POST" });
      setActiveThemeId(themeId);
    } catch {}
  };

  return (
    <AdminLayout>
      <Head><title>Themes — Admin</title></Head>
      <div className="admin-header">
        <h1>Themes (300)</h1>
      </div>

      {/* Category filter */}
      <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap", marginBottom: "1.5rem" }}>
        <button className={`admin-btn ${!activeFilter ? "admin-btn-primary" : "admin-btn-outline"}`} onClick={() => { setActiveFilter(""); setPage(0); }}>
          All
        </button>
        {categories.map((c) => (
          <button key={c.category} className={`admin-btn ${activeFilter === c.category ? "admin-btn-primary" : "admin-btn-outline"}`} onClick={() => { setActiveFilter(c.category); setPage(0); }}>
            {c.category} ({c.count})
          </button>
        ))}
      </div>

      {/* Theme grid */}
      <div className="theme-grid">
        {themes.map((theme) => (
          <div
            key={theme.id}
            className={`theme-card ${activeThemeId === theme.id ? "active" : ""}`}
            onClick={() => activate(theme.id)}
          >
            <div className="theme-preview">
              <div className="theme-preview-header" style={{ background: theme.header_bg }} />
              <div className="theme-preview-body" style={{ background: theme.bg_color, color: theme.text_color }}>
                <span style={{ color: theme.primary_color, fontWeight: 600, fontSize: "0.8rem" }}>Aa</span>
                <span style={{ color: theme.accent_color, marginLeft: 8, fontSize: "0.7rem" }}>btn</span>
              </div>
              <div className="theme-preview-footer" style={{ background: theme.footer_bg }} />
            </div>
            <div className="theme-card-info">
              <div>{theme.name}</div>
              <div style={{ fontSize: "0.7rem", color: "#6b7280" }}>
                {theme.font_family} / {theme.layout_style}
              </div>
              {activeThemeId === theme.id && (
                <div style={{ color: "#059669", fontWeight: 600, fontSize: "0.75rem", marginTop: 2 }}>Active</div>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Pagination */}
      <div style={{ display: "flex", gap: "0.5rem", justifyContent: "center", marginTop: "2rem" }}>
        <button className="admin-btn admin-btn-outline" disabled={page === 0} onClick={() => setPage((p) => p - 1)}>Previous</button>
        <span style={{ padding: "0.5rem 1rem", color: "#6b7280" }}>Page {page + 1}</span>
        <button className="admin-btn admin-btn-outline" disabled={themes.length < PAGE_SIZE} onClick={() => setPage((p) => p + 1)}>Next</button>
      </div>
    </AdminLayout>
  );
}

Themes.isAdmin = true;
export default Themes;
