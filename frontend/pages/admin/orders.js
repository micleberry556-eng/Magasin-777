/**
 * Admin orders management.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

const STATUSES = ["new", "processing", "shipped", "delivered", "cancelled"];

function Orders() {
  const { adminFetch } = useAdmin();
  const [orders, setOrders] = useState([]);
  const [detail, setDetail] = useState(null);
  const [filter, setFilter] = useState("");

  const load = () => {
    let url = "/api/admin/orders?limit=200";
    if (filter) url += `&status=${filter}`;
    adminFetch(url).then(setOrders).catch(() => {});
  };
  useEffect(load, [adminFetch, filter]);

  const updateStatus = async (orderId, status) => {
    await adminFetch(`/api/admin/orders/${orderId}/status`, { method: "PATCH", body: JSON.stringify({ status }) }).catch(() => {});
    load();
    if (detail?.id === orderId) {
      setDetail((d) => ({ ...d, status }));
    }
  };

  const badgeClass = (s) => `badge badge-${s}`;

  if (detail) {
    return (
      <AdminLayout>
        <Head><title>Order #{detail.id} — Admin</title></Head>
        <div className="admin-header">
          <h1>Order #{detail.id}</h1>
          <button className="admin-btn admin-btn-outline" onClick={() => setDetail(null)}>Back</button>
        </div>
        <div className="admin-form">
          <p><strong>Customer:</strong> {detail.customer_name}</p>
          <p><strong>Email:</strong> {detail.customer_email}</p>
          <p><strong>Phone:</strong> {detail.customer_phone}</p>
          <p><strong>Address:</strong> {detail.customer_address}</p>
          <p><strong>Note:</strong> {detail.note}</p>
          <p><strong>Status:</strong> <span className={badgeClass(detail.status)}>{detail.status}</span></p>
          <p><strong>Total:</strong> ${detail.total_amount}</p>
          <p><strong>Date:</strong> {new Date(detail.created_at).toLocaleString()}</p>

          <h3 style={{ marginTop: "1.5rem", marginBottom: "0.5rem" }}>Items</h3>
          <table className="admin-table">
            <thead><tr><th>Product</th><th>Qty</th><th>Price</th><th>Subtotal</th></tr></thead>
            <tbody>
              {detail.items.map((item) => (
                <tr key={item.id}>
                  <td>{item.product_name}</td>
                  <td>{item.quantity}</td>
                  <td>${item.price}</td>
                  <td>${(item.price * item.quantity).toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <h3 style={{ marginTop: "1.5rem", marginBottom: "0.5rem" }}>Change Status</h3>
          <div style={{ display: "flex", gap: "0.5rem", flexWrap: "wrap" }}>
            {STATUSES.map((s) => (
              <button key={s} className={`admin-btn ${detail.status === s ? "admin-btn-primary" : "admin-btn-outline"}`} onClick={() => updateStatus(detail.id, s)}>
                {s}
              </button>
            ))}
          </div>
        </div>
      </AdminLayout>
    );
  }

  return (
    <AdminLayout>
      <Head><title>Orders — Admin</title></Head>
      <div className="admin-header">
        <h1>Orders ({orders.length})</h1>
        <div style={{ display: "flex", gap: "0.5rem" }}>
          <select className="form-input" style={{ width: "auto" }} value={filter} onChange={(e) => setFilter(e.target.value)}>
            <option value="">All</option>
            {STATUSES.map((s) => <option key={s} value={s}>{s}</option>)}
          </select>
        </div>
      </div>
      <table className="admin-table">
        <thead><tr><th>ID</th><th>Customer</th><th>Total</th><th>Status</th><th>Date</th><th>Actions</th></tr></thead>
        <tbody>
          {orders.map((o) => (
            <tr key={o.id}>
              <td>#{o.id}</td>
              <td>{o.customer_name}</td>
              <td>${o.total_amount}</td>
              <td><span className={badgeClass(o.status)}>{o.status}</span></td>
              <td>{new Date(o.created_at).toLocaleDateString()}</td>
              <td><button className="admin-btn admin-btn-outline" onClick={() => setDetail(o)}>View</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </AdminLayout>
  );
}

Orders.isAdmin = true;
export default Orders;
