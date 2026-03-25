/**
 * Admin login page.
 */
import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import Head from "next/head";
import { useAdmin } from "../../lib/useAdmin";

function AdminLogin() {
  const { token, login } = useAdmin();
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (token) router.push("/admin/dashboard");
  }, [token, router]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await login(email, password);
      router.push("/admin/dashboard");
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  return (
    <>
      <Head><title>Admin Login</title></Head>
      <div className="admin-login">
        <div className="admin-login-card">
          <h1>Admin Panel</h1>
          {error && <div className="alert alert-error">{error}</div>}
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label className="form-label">Email</label>
              <input className="form-input" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            </div>
            <div className="form-group">
              <label className="form-label">Password</label>
              <input className="form-input" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            </div>
            <button className="admin-btn admin-btn-primary" style={{ width: "100%" }} disabled={loading}>
              {loading ? "..." : "Login"}
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

AdminLogin.isAdmin = true;
export default AdminLogin;
