/**
 * Admin dashboard — overview stats.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

function Dashboard() {
  const { adminFetch } = useAdmin();
  const [stats, setStats] = useState({ products: 0, orders: 0, stock: null });

  useEffect(() => {
    Promise.all([
      adminFetch("/api/admin/products?limit=1").then((r) => r.length !== undefined ? r : []),
      adminFetch("/api/admin/orders?limit=1").then((r) => r.length !== undefined ? r : []),
      adminFetch("/api/admin/stock/summary").catch(() => null),
    ]).then(([products, orders, stock]) => {
      setStats({ products: products.length, orders: orders.length, stock });
    }).catch(() => {});
  }, [adminFetch]);

  return (
    <AdminLayout>
      <Head><title>Dashboard — Admin</title></Head>
      <div className="admin-header"><h1>Dashboard</h1></div>

      <div className="admin-stats">
        <div className="admin-stat-card">
          <div className="label">Total Products</div>
          <div className="value">{stats.stock?.total_products ?? "—"}</div>
        </div>
        <div className="admin-stat-card">
          <div className="label">Total Stock</div>
          <div className="value">{stats.stock?.total_stock ?? "—"}</div>
        </div>
        <div className="admin-stat-card">
          <div className="label">Low Stock Items</div>
          <div className="value">{stats.stock?.low_stock_items?.length ?? "—"}</div>
        </div>
      </div>

      {stats.stock?.low_stock_items?.length > 0 && (
        <div>
          <h3 style={{ marginBottom: "0.75rem" }}>Low Stock Alert</h3>
          <table className="admin-table">
            <thead>
              <tr><th>Product</th><th>SKU</th><th>Stock</th></tr>
            </thead>
            <tbody>
              {stats.stock.low_stock_items.map((item) => (
                <tr key={item.id}>
                  <td>{item.name}</td>
                  <td>{item.sku}</td>
                  <td style={{ color: item.stock <= 0 ? "#dc2626" : "#f59e0b", fontWeight: 600 }}>{item.stock}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </AdminLayout>
  );
}

Dashboard.isAdmin = true;
export default Dashboard;
