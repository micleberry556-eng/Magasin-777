/**
 * Admin site settings — name, SEO, language, contact, background upload.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import AdminLayout from "../../components/admin/AdminLayout";
import { useAdmin } from "../../lib/useAdmin";

const LANGUAGES = [
  { code: "ru", name: "Русский" }, { code: "en", name: "English" },
  { code: "kk", name: "Қазақша" }, { code: "uz", name: "O'zbek" },
  { code: "tg", name: "Тоҷикӣ" }, { code: "ky", name: "Кыргызча" },
  { code: "az", name: "Azərbaycan" }, { code: "tr", name: "Türkçe" },
  { code: "zh", name: "中文" }, { code: "ms", name: "Bahasa Melayu" },
  { code: "th", name: "ไทย" }, { code: "vi", name: "Tiếng Việt" },
  { code: "id", name: "Bahasa Indonesia" },
];

const CURRENCIES = ["USD", "EUR", "RUB", "KZT", "UZS", "TJS", "KGS", "AZN", "TRY", "CNY", "MYR", "THB", "VND", "IDR"];

function Settings() {
  const { token, adminFetch, loading } = useAdmin();
  const [form, setForm] = useState(null);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);
  const [uploading, setUploading] = useState(false);

  useEffect(() => {
    if (loading || !token) return;
    adminFetch("/api/settings").then((r) => r && setForm(r)).catch(() => {});
  }, [loading, token]);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSave = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess(false);
    try {
      const updated = await adminFetch("/api/admin/settings", { method: "PATCH", body: JSON.stringify(form) });
      setForm(updated);
      setSuccess(true);
    } catch (err) { setError(err.message); }
  };

  const handleUpload = async (e, field) => {
    const file = e.target.files[0];
    if (!file) return;
    setUploading(true);
    try {
      const formData = new FormData();
      formData.append("file", file);
      const res = await fetch("/api/admin/upload", {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });
      if (!res.ok) throw new Error("Upload failed");
      const data = await res.json();
      setForm((f) => ({ ...f, [field]: data.url }));
    } catch (err) { setError(err.message); }
    setUploading(false);
  };

  if (!form) return <AdminLayout><p>Loading...</p></AdminLayout>;

  return (
    <AdminLayout>
      <Head><title>Site Settings — Admin</title></Head>
      <div className="admin-header"><h1>Site Settings</h1></div>

      <form className="admin-form" onSubmit={handleSave} style={{ maxWidth: 800 }}>
        {error && <div className="alert alert-error">{error}</div>}
        {success && <div className="alert alert-success">Settings saved!</div>}

        {/* General */}
        <h3 style={{ marginBottom: "1rem", paddingBottom: "0.5rem", borderBottom: "1px solid #e2e8f0" }}>General</h3>
        <div className="form-group"><label className="form-label">Site Name</label><input className="form-input" name="site_name" value={form.site_name} onChange={handleChange} /></div>
        <div className="form-group"><label className="form-label">Site Description</label><textarea className="form-input" name="site_description" rows={2} value={form.site_description} onChange={handleChange} /></div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem" }}>
          <div className="form-group">
            <label className="form-label">Default Language</label>
            <select className="form-input" name="default_language" value={form.default_language} onChange={handleChange}>
              {LANGUAGES.map((l) => <option key={l.code} value={l.code}>{l.name}</option>)}
            </select>
          </div>
          <div className="form-group">
            <label className="form-label">Currency</label>
            <select className="form-input" name="currency" value={form.currency} onChange={handleChange}>
              {CURRENCIES.map((c) => <option key={c} value={c}>{c}</option>)}
            </select>
          </div>
        </div>

        {/* SEO */}
        <h3 style={{ marginTop: "1.5rem", marginBottom: "1rem", paddingBottom: "0.5rem", borderBottom: "1px solid #e2e8f0" }}>SEO</h3>
        <div className="form-group"><label className="form-label">SEO Title</label><input className="form-input" name="seo_title" value={form.seo_title} onChange={handleChange} /></div>
        <div className="form-group"><label className="form-label">SEO Description</label><textarea className="form-input" name="seo_description" rows={2} value={form.seo_description} onChange={handleChange} /></div>
        <div className="form-group"><label className="form-label">SEO Keywords</label><input className="form-input" name="seo_keywords" value={form.seo_keywords} onChange={handleChange} placeholder="keyword1, keyword2, keyword3" /></div>
        <div className="form-group"><label className="form-label">Analytics Code (HTML)</label><textarea className="form-input" name="analytics_code" rows={3} value={form.analytics_code} onChange={handleChange} placeholder="<!-- Google Analytics -->" /></div>

        {/* Branding */}
        <h3 style={{ marginTop: "1.5rem", marginBottom: "1rem", paddingBottom: "0.5rem", borderBottom: "1px solid #e2e8f0" }}>Branding &amp; Background</h3>
        <div className="form-group">
          <label className="form-label">Logo</label>
          <div style={{ display: "flex", gap: "0.5rem", alignItems: "center" }}>
            <input className="form-input" name="logo_url" value={form.logo_url} onChange={handleChange} placeholder="URL or upload" style={{ flex: 1 }} />
            <label className="admin-btn admin-btn-outline" style={{ cursor: "pointer", whiteSpace: "nowrap" }}>
              Upload <input type="file" accept="image/*" hidden onChange={(e) => handleUpload(e, "logo_url")} />
            </label>
          </div>
          {form.logo_url && <img src={form.logo_url} alt="Logo" style={{ height: 40, marginTop: "0.5rem" }} />}
        </div>
        <div className="form-group">
          <label className="form-label">Favicon</label>
          <div style={{ display: "flex", gap: "0.5rem", alignItems: "center" }}>
            <input className="form-input" name="favicon_url" value={form.favicon_url} onChange={handleChange} style={{ flex: 1 }} />
            <label className="admin-btn admin-btn-outline" style={{ cursor: "pointer", whiteSpace: "nowrap" }}>
              Upload <input type="file" accept="image/*" hidden onChange={(e) => handleUpload(e, "favicon_url")} />
            </label>
          </div>
        </div>
        <div className="form-group">
          <label className="form-label">Background Image</label>
          <div style={{ display: "flex", gap: "0.5rem", alignItems: "center" }}>
            <input className="form-input" name="background_url" value={form.background_url} onChange={handleChange} style={{ flex: 1 }} />
            <label className="admin-btn admin-btn-outline" style={{ cursor: "pointer", whiteSpace: "nowrap" }}>
              {uploading ? "..." : "Upload"} <input type="file" accept="image/*" hidden onChange={(e) => handleUpload(e, "background_url")} />
            </label>
          </div>
          {form.background_url && <img src={form.background_url} alt="Background" style={{ height: 80, marginTop: "0.5rem", borderRadius: 8, objectFit: "cover" }} />}
        </div>

        {/* Contact */}
        <h3 style={{ marginTop: "1.5rem", marginBottom: "1rem", paddingBottom: "0.5rem", borderBottom: "1px solid #e2e8f0" }}>Contact Info</h3>
        <div className="form-group"><label className="form-label">Email</label><input className="form-input" name="contact_email" value={form.contact_email} onChange={handleChange} /></div>
        <div className="form-group"><label className="form-label">Phone</label><input className="form-input" name="contact_phone" value={form.contact_phone} onChange={handleChange} /></div>
        <div className="form-group"><label className="form-label">Address</label><textarea className="form-input" name="contact_address" rows={2} value={form.contact_address} onChange={handleChange} /></div>

        <button className="admin-btn admin-btn-primary" type="submit" style={{ marginTop: "1rem" }}>Save Settings</button>
      </form>
    </AdminLayout>
  );
}

Settings.isAdmin = true;
export default Settings;
