/**
 * Admin categories management.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

const EMPTY = { name: "", slug: "", parent_id: "", image: "", sort_order: "0" };

function Categories() {
  const { adminFetch } = useAdmin();
  const [categories, setCategories] = useState([]);
  const [editing, setEditing] = useState(null);
  const [form, setForm] = useState(EMPTY);
  const [error, setError] = useState("");

  const load = () => adminFetch("/api/categories").then(setCategories).catch(() => {});
  useEffect(load, [adminFetch]);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSave = async (e) => {
    e.preventDefault();
    setError("");
    const body = { ...form, sort_order: parseInt(form.sort_order) || 0, parent_id: form.parent_id ? parseInt(form.parent_id) : null };
    try {
      if (editing === "new") {
        await adminFetch("/api/admin/categories", { method: "POST", body: JSON.stringify(body) });
      } else {
        await adminFetch(`/api/admin/categories/${editing}`, { method: "PATCH", body: JSON.stringify(body) });
      }
      setEditing(null);
      load();
    } catch (err) { setError(err.message); }
  };

  const handleDelete = async (id) => {
    if (!confirm("Delete this category?")) return;
    await adminFetch(`/api/admin/categories/${id}`, { method: "DELETE" }).catch(() => {});
    load();
  };

  if (editing !== null) {
    return (
      <AdminLayout>
        <Head><title>{editing === "new" ? "New Category" : "Edit Category"} — Admin</title></Head>
        <div className="admin-header">
          <h1>{editing === "new" ? "New Category" : "Edit Category"}</h1>
          <button className="admin-btn admin-btn-outline" onClick={() => setEditing(null)}>Back</button>
        </div>
        <form className="admin-form" onSubmit={handleSave}>
          {error && <div className="alert alert-error">{error}</div>}
          <div className="form-group"><label className="form-label">Name *</label><input className="form-input" name="name" value={form.name} onChange={handleChange} required /></div>
          <div className="form-group"><label className="form-label">Slug *</label><input className="form-input" name="slug" value={form.slug} onChange={handleChange} required /></div>
          <div className="form-group"><label className="form-label">Image URL</label><input className="form-input" name="image" value={form.image} onChange={handleChange} /></div>
          <div className="form-group"><label className="form-label">Sort Order</label><input className="form-input" name="sort_order" type="number" value={form.sort_order} onChange={handleChange} /></div>
          <button className="admin-btn admin-btn-primary" type="submit">Save</button>
        </form>
      </AdminLayout>
    );
  }

  return (
    <AdminLayout>
      <Head><title>Categories — Admin</title></Head>
      <div className="admin-header">
        <h1>Categories ({categories.length})</h1>
        <button className="admin-btn admin-btn-primary" onClick={() => { setEditing("new"); setForm(EMPTY); }}>+ Add Category</button>
      </div>
      <table className="admin-table">
        <thead><tr><th>ID</th><th>Name</th><th>Slug</th><th>Sort</th><th>Actions</th></tr></thead>
        <tbody>
          {categories.map((c) => (
            <tr key={c.id}>
              <td>{c.id}</td>
              <td>{c.name}</td>
              <td>{c.slug}</td>
              <td>{c.sort_order}</td>
              <td>
                <button className="admin-btn admin-btn-outline" style={{ marginRight: "0.5rem" }} onClick={() => { setEditing(c.id); setForm({ ...EMPTY, ...c, sort_order: String(c.sort_order), parent_id: c.parent_id ? String(c.parent_id) : "" }); }}>Edit</button>
                <button className="admin-btn admin-btn-danger" onClick={() => handleDelete(c.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </AdminLayout>
  );
}

Categories.isAdmin = true;
export default Categories;
