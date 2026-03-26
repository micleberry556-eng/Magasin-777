/**
 * Admin CMS pages management.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

const EMPTY = { title: "", slug: "", content: "", is_published: true, sort_order: "0", seo_title: "", seo_description: "" };

function Pages() {
  const { adminFetch, loading, token } = useAdmin();
  const [pages, setPages] = useState([]);
  const [editing, setEditing] = useState(null);
  const [form, setForm] = useState(EMPTY);
  const [error, setError] = useState("");

  const load = () => { if (!token) return; adminFetch("/api/admin/pages").then((r) => r && setPages(r)).catch(() => {}); };
  useEffect(() => { if (!loading && token) load(); }, [loading, token]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm((f) => ({ ...f, [name]: type === "checkbox" ? checked : value }));
  };

  const handleSave = async (e) => {
    e.preventDefault();
    setError("");
    const body = { ...form, sort_order: parseInt(form.sort_order) || 0 };
    try {
      if (editing === "new") {
        await adminFetch("/api/admin/pages", { method: "POST", body: JSON.stringify(body) });
      } else {
        await adminFetch(`/api/admin/pages/${editing}`, { method: "PATCH", body: JSON.stringify(body) });
      }
      setEditing(null);
      load();
    } catch (err) { setError(err.message); }
  };

  const handleDelete = async (id) => {
    if (!confirm("Delete this page?")) return;
    await adminFetch(`/api/admin/pages/${id}`, { method: "DELETE" }).catch(() => {});
    load();
  };

  if (editing !== null) {
    return (
      <AdminLayout>
        <Head><title>{editing === "new" ? "New Page" : "Edit Page"} — Admin</title></Head>
        <div className="admin-header">
          <h1>{editing === "new" ? "New Page" : "Edit Page"}</h1>
          <button className="admin-btn admin-btn-outline" onClick={() => setEditing(null)}>Back</button>
        </div>
        <form className="admin-form" onSubmit={handleSave} style={{ maxWidth: 800 }}>
          {error && <div className="alert alert-error">{error}</div>}
          <div className="form-group"><label className="form-label">Title *</label><input className="form-input" name="title" value={form.title} onChange={handleChange} required /></div>
          <div className="form-group"><label className="form-label">Slug *</label><input className="form-input" name="slug" value={form.slug} onChange={handleChange} required /></div>
          <div className="form-group"><label className="form-label">Content (HTML)</label><textarea className="form-input" name="content" rows={12} value={form.content} onChange={handleChange} /></div>
          <div className="form-group"><label className="form-label">SEO Title</label><input className="form-input" name="seo_title" value={form.seo_title} onChange={handleChange} /></div>
          <div className="form-group"><label className="form-label">SEO Description</label><input className="form-input" name="seo_description" value={form.seo_description} onChange={handleChange} /></div>
          <div style={{ display: "flex", gap: "1rem", marginBottom: "1rem" }}>
            <div className="form-group"><label className="form-label">Sort Order</label><input className="form-input" name="sort_order" type="number" value={form.sort_order} onChange={handleChange} style={{ width: 100 }} /></div>
            <label style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}><input type="checkbox" name="is_published" checked={form.is_published} onChange={handleChange} /> Published</label>
          </div>
          <button className="admin-btn admin-btn-primary" type="submit">Save</button>
        </form>
      </AdminLayout>
    );
  }

  return (
    <AdminLayout>
      <Head><title>Pages — Admin</title></Head>
      <div className="admin-header">
        <h1>Pages ({pages.length})</h1>
        <button className="admin-btn admin-btn-primary" onClick={() => { setEditing("new"); setForm(EMPTY); }}>+ Add Page</button>
      </div>
      <table className="admin-table">
        <thead><tr><th>ID</th><th>Title</th><th>Slug</th><th>Published</th><th>Actions</th></tr></thead>
        <tbody>
          {pages.map((p) => (
            <tr key={p.id}>
              <td>{p.id}</td>
              <td>{p.title}</td>
              <td>/page/{p.slug}</td>
              <td>{p.is_published ? "Yes" : "No"}</td>
              <td>
                <button className="admin-btn admin-btn-outline" style={{ marginRight: "0.5rem" }} onClick={() => { setEditing(p.id); setForm({ ...EMPTY, ...p, sort_order: String(p.sort_order) }); }}>Edit</button>
                <button className="admin-btn admin-btn-danger" onClick={() => handleDelete(p.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </AdminLayout>
  );
}

Pages.isAdmin = true;
export default Pages;
