/**
 * Admin products management — list, create, edit, delete.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

const EMPTY = { name: "", slug: "", description: "", price: "", old_price: "", sku: "", stock: "0", category_id: "", image: "", is_active: true, is_featured: false, seo_title: "", seo_description: "" };

function Products() {
  const { adminFetch, loading, token } = useAdmin();
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [editing, setEditing] = useState(null); // null=list, "new"=create, id=edit
  const [form, setForm] = useState(EMPTY);
  const [error, setError] = useState("");

  const load = () => {
    if (!token) return;
    adminFetch("/api/admin/products?limit=200").then((r) => r && setProducts(r)).catch(() => {});
    adminFetch("/api/categories").then((r) => r && setCategories(r)).catch(() => {});
  };
  useEffect(() => { if (!loading && token) load(); }, [loading, token]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm((f) => ({ ...f, [name]: type === "checkbox" ? checked : value }));
  };

  const handleEdit = (p) => {
    setEditing(p.id);
    setForm({ ...EMPTY, ...p, price: String(p.price), old_price: p.old_price ? String(p.old_price) : "", stock: String(p.stock), category_id: p.category_id ? String(p.category_id) : "" });
  };

  const handleSave = async (e) => {
    e.preventDefault();
    setError("");
    const body = { ...form, price: parseFloat(form.price), stock: parseInt(form.stock), category_id: form.category_id ? parseInt(form.category_id) : null, old_price: form.old_price ? parseFloat(form.old_price) : null };
    try {
      if (editing === "new") {
        await adminFetch("/api/admin/products", { method: "POST", body: JSON.stringify(body) });
      } else {
        await adminFetch(`/api/admin/products/${editing}`, { method: "PATCH", body: JSON.stringify(body) });
      }
      setEditing(null);
      load();
    } catch (err) { setError(err.message); }
  };

  const handleDelete = async (id) => {
    if (!confirm("Delete this product?")) return;
    await adminFetch(`/api/admin/products/${id}`, { method: "DELETE" }).catch(() => {});
    load();
  };

  if (editing !== null) {
    return (
      <AdminLayout>
        <Head><title>{editing === "new" ? "New Product" : "Edit Product"} — Admin</title></Head>
        <div className="admin-header">
          <h1>{editing === "new" ? "New Product" : "Edit Product"}</h1>
          <button className="admin-btn admin-btn-outline" onClick={() => setEditing(null)}>Back</button>
        </div>
        <form className="admin-form" onSubmit={handleSave}>
          {error && <div className="alert alert-error">{error}</div>}
          <div className="form-group"><label className="form-label">Name *</label><input className="form-input" name="name" value={form.name} onChange={handleChange} required /></div>
          <div className="form-group"><label className="form-label">Slug *</label><input className="form-input" name="slug" value={form.slug} onChange={handleChange} required /></div>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "1rem" }}>
            <div className="form-group"><label className="form-label">Price *</label><input className="form-input" name="price" type="number" step="0.01" value={form.price} onChange={handleChange} required /></div>
            <div className="form-group"><label className="form-label">Old Price</label><input className="form-input" name="old_price" type="number" step="0.01" value={form.old_price} onChange={handleChange} /></div>
            <div className="form-group"><label className="form-label">Stock</label><input className="form-input" name="stock" type="number" value={form.stock} onChange={handleChange} /></div>
          </div>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem" }}>
            <div className="form-group"><label className="form-label">SKU</label><input className="form-input" name="sku" value={form.sku} onChange={handleChange} /></div>
            <div className="form-group">
              <label className="form-label">Category</label>
              <select className="form-input" name="category_id" value={form.category_id} onChange={handleChange}>
                <option value="">— None —</option>
                {categories.map((c) => <option key={c.id} value={c.id}>{c.name}</option>)}
              </select>
            </div>
          </div>
          <div className="form-group"><label className="form-label">Image URL</label><input className="form-input" name="image" value={form.image} onChange={handleChange} /></div>
          <div className="form-group"><label className="form-label">Description</label><textarea className="form-input" name="description" rows={4} value={form.description} onChange={handleChange} /></div>
          <div className="form-group"><label className="form-label">SEO Title</label><input className="form-input" name="seo_title" value={form.seo_title} onChange={handleChange} /></div>
          <div className="form-group"><label className="form-label">SEO Description</label><input className="form-input" name="seo_description" value={form.seo_description} onChange={handleChange} /></div>
          <div style={{ display: "flex", gap: "1rem", marginBottom: "1rem" }}>
            <label><input type="checkbox" name="is_active" checked={form.is_active} onChange={handleChange} /> Active</label>
            <label><input type="checkbox" name="is_featured" checked={form.is_featured} onChange={handleChange} /> Featured</label>
          </div>
          <button className="admin-btn admin-btn-primary" type="submit">Save</button>
        </form>
      </AdminLayout>
    );
  }

  return (
    <AdminLayout>
      <Head><title>Products — Admin</title></Head>
      <div className="admin-header">
        <h1>Products ({products.length})</h1>
        <button className="admin-btn admin-btn-primary" onClick={() => { setEditing("new"); setForm(EMPTY); }}>+ Add Product</button>
      </div>
      <table className="admin-table">
        <thead><tr><th>ID</th><th>Name</th><th>Price</th><th>Stock</th><th>Active</th><th>Actions</th></tr></thead>
        <tbody>
          {products.map((p) => (
            <tr key={p.id}>
              <td>{p.id}</td>
              <td>{p.name}</td>
              <td>${p.price}</td>
              <td style={{ color: p.stock < 10 ? "#dc2626" : "inherit" }}>{p.stock}</td>
              <td>{p.is_active ? "Yes" : "No"}</td>
              <td>
                <button className="admin-btn admin-btn-outline" style={{ marginRight: "0.5rem" }} onClick={() => handleEdit(p)}>Edit</button>
                <button className="admin-btn admin-btn-danger" onClick={() => handleDelete(p.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </AdminLayout>
  );
}

Products.isAdmin = true;
export default Products;
