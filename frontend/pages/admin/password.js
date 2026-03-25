/**
 * Admin change password page.
 */
import { useState } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

function ChangePassword() {
  const { adminFetch } = useAdmin();
  const [form, setForm] = useState({ current_password: "", new_password: "", confirm: "" });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess(false);
    if (form.new_password !== form.confirm) {
      setError("Passwords do not match");
      return;
    }
    if (form.new_password.length < 6) {
      setError("Password must be at least 6 characters");
      return;
    }
    try {
      await adminFetch("/api/admin/change-password", {
        method: "POST",
        body: JSON.stringify({ current_password: form.current_password, new_password: form.new_password }),
      });
      setSuccess(true);
      setForm({ current_password: "", new_password: "", confirm: "" });
    } catch (err) { setError(err.message); }
  };

  return (
    <AdminLayout>
      <Head><title>Change Password — Admin</title></Head>
      <div className="admin-header"><h1>Change Password</h1></div>
      <form className="admin-form" onSubmit={handleSubmit}>
        {error && <div className="alert alert-error">{error}</div>}
        {success && <div className="alert alert-success">Password changed successfully!</div>}
        <div className="form-group"><label className="form-label">Current Password</label><input className="form-input" type="password" value={form.current_password} onChange={(e) => setForm({ ...form, current_password: e.target.value })} required /></div>
        <div className="form-group"><label className="form-label">New Password</label><input className="form-input" type="password" value={form.new_password} onChange={(e) => setForm({ ...form, new_password: e.target.value })} required /></div>
        <div className="form-group"><label className="form-label">Confirm New Password</label><input className="form-input" type="password" value={form.confirm} onChange={(e) => setForm({ ...form, confirm: e.target.value })} required /></div>
        <button className="admin-btn admin-btn-primary" type="submit">Change Password</button>
      </form>
    </AdminLayout>
  );
}

ChangePassword.isAdmin = true;
export default ChangePassword;
