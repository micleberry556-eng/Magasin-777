/**
 * Admin panel layout with sidebar navigation.
 */
import Link from "next/link";
import { useRouter } from "next/router";
import { useAdmin } from "../../lib/useAdmin";

export default function AdminLayout({ children }) {
  const { token, loading, logout } = useAdmin();
  const router = useRouter();

  if (loading) return <div className="admin-login"><p style={{ color: "#fff" }}>Loading...</p></div>;

  if (!token) {
    if (typeof window !== "undefined") router.push("/admin");
    return null;
  }

  const isActive = (path) => router.pathname === path ? "active" : "";

  return (
    <div className="admin-layout">
      <aside className="admin-sidebar">
        <div className="admin-sidebar-logo">Admin Panel</div>
        <ul className="admin-nav">
          <li><Link href="/admin/dashboard" className={isActive("/admin/dashboard")}>Dashboard</Link></li>

          <li className="admin-nav-section">Catalog</li>
          <li><Link href="/admin/products" className={isActive("/admin/products")}>Products</Link></li>
          <li><Link href="/admin/categories" className={isActive("/admin/categories")}>Categories</Link></li>

          <li className="admin-nav-section">Sales</li>
          <li><Link href="/admin/orders" className={isActive("/admin/orders")}>Orders</Link></li>
          <li><Link href="/admin/stock" className={isActive("/admin/stock")}>Inventory</Link></li>

          <li className="admin-nav-section">Content</li>
          <li><Link href="/admin/pages" className={isActive("/admin/pages")}>Pages</Link></li>

          <li className="admin-nav-section">Appearance</li>
          <li><Link href="/admin/themes" className={isActive("/admin/themes")}>Themes (300)</Link></li>
          <li><Link href="/admin/settings" className={isActive("/admin/settings")}>Site Settings</Link></li>

          <li className="admin-nav-section">Account</li>
          <li><Link href="/admin/password" className={isActive("/admin/password")}>Change Password</Link></li>
          <li>
            <a href="#" onClick={(e) => { e.preventDefault(); logout(); router.push("/admin"); }}>
              Logout
            </a>
          </li>
        </ul>
      </aside>
      <div className="admin-main">{children}</div>
    </div>
  );
}
