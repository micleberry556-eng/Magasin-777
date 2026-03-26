/**
 * Admin inventory / stock management.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

function Stock() {
  const { adminFetch, loading, token } = useAdmin();
  const [movements, setMovements] = useState([]);
  const [summary, setSummary] = useState(null);
  const [products, setProducts] = useState([]);
  const [form, setForm] = useState({ product_id: "", quantity: "", reason: "purchase", note: "" });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  const load = () => {
    if (!token) return;
    adminFetch("/api/admin/stock?limit=100").then((r) => r && setMovements(r)).catch(() => {});
    adminFetch("/api/admin/stock/summary").then((r) => r && setSummary(r)).catch(() => {});
    adminFetch("/api/admin/products?limit=500").then((r) => r && setProducts(r)).catch(() => {});
  };
  useEffect(() => { if (!loading && token) load(); }, [loading, token]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess(false);
    try {
      await adminFetch("/api/admin/stock", {
        method: "POST",
        body: JSON.stringify({
          product_id: parseInt(form.product_id),
          quantity: parseInt(form.quantity),
          reason: form.reason,
          note: form.note,
        }),
      });
      setSuccess(true);
      setForm({ product_id: "", quantity: "", reason: "purchase", note: "" });
      load();
    } catch (err) { setError(err.message); }
  };

  return (
    <AdminLayout>
      <Head><title>Inventory — Admin</title></Head>
      <div className="admin-header"><h1>Inventory Management</h1></div>

      {/* Summary */}
      {summary && (
        <div className="admin-stats">
          <div className="admin-stat-card"><div className="label">Total Products</div><div className="value">{summary.total_products}</div></div>
          <div className="admin-stat-card"><div className="label">Total Stock</div><div className="value">{summary.total_stock}</div></div>
          <div className="admin-stat-card"><div className="label">Low Stock</div><div className="value" style={{ color: summary.low_stock_items.length > 0 ? "#dc2626" : "inherit" }}>{summary.low_stock_items.length}</div></div>
        </div>
      )}

      {/* Add movement form */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "2rem" }}>
        <div>
          <h3 style={{ marginBottom: "1rem" }}>Record Stock Movement</h3>
          <form className="admin-form" onSubmit={handleSubmit}>
            {error && <div className="alert alert-error">{error}</div>}
            {success && <div className="alert alert-success">Stock updated!</div>}
            <div className="form-group">
              <label className="form-label">Product *</label>
              <select className="form-input" value={form.product_id} onChange={(e) => setForm({ ...form, product_id: e.target.value })} required>
                <option value="">Select product...</option>
                {products.map((p) => <option key={p.id} value={p.id}>{p.name} (stock: {p.stock})</option>)}
              </select>
            </div>
            <div className="form-group">
              <label className="form-label">Quantity * (positive = in, negative = out)</label>
              <input className="form-input" type="number" value={form.quantity} onChange={(e) => setForm({ ...form, quantity: e.target.value })} required />
            </div>
            <div className="form-group">
              <label className="form-label">Reason</label>
              <select className="form-input" value={form.reason} onChange={(e) => setForm({ ...form, reason: e.target.value })}>
                <option value="purchase">Purchase (incoming)</option>
                <option value="return">Return (incoming)</option>
                <option value="adjustment">Adjustment</option>
                <option value="sale">Manual Sale (outgoing)</option>
              </select>
            </div>
            <div className="form-group"><label className="form-label">Note</label><input className="form-input" value={form.note} onChange={(e) => setForm({ ...form, note: e.target.value })} /></div>
            <button className="admin-btn admin-btn-primary" type="submit">Record Movement</button>
          </form>
        </div>

        {/* Recent movements */}
        <div>
          <h3 style={{ marginBottom: "1rem" }}>Recent Movements</h3>
          <table className="admin-table">
            <thead><tr><th>Date</th><th>Product</th><th>Qty</th><th>Reason</th><th>Note</th></tr></thead>
            <tbody>
              {movements.slice(0, 20).map((m) => {
                const prod = products.find((p) => p.id === m.product_id);
                return (
                  <tr key={m.id}>
                    <td>{new Date(m.created_at).toLocaleDateString()}</td>
                    <td>{prod?.name || `#${m.product_id}`}</td>
                    <td style={{ color: m.quantity > 0 ? "#059669" : "#dc2626", fontWeight: 600 }}>
                      {m.quantity > 0 ? `+${m.quantity}` : m.quantity}
                    </td>
                    <td>{m.reason}</td>
                    <td>{m.note}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </AdminLayout>
  );
}

Stock.isAdmin = true;
export default Stock;
