/**
 * Checkout page — order form.
 */
import { useState } from "react";
import Head from "next/head";
import Link from "next/link";
import { useCart } from "../../lib/useCart";
import { useLang } from "../../lib/useLang";

export default function Checkout() {
  const { items, total, clearCart } = useCart();
  const { t } = useLang();
  const [form, setForm] = useState({ customer_name: "", customer_email: "", customer_phone: "", customer_address: "", note: "" });
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (items.length === 0) return;
    setLoading(true);
    setError("");
    try {
      const res = await fetch("/api/orders", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...form,
          items: items.map((i) => ({ product_id: i.id, quantity: i.qty })),
        }),
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || "Order failed");
      }
      setSuccess(true);
      clearCart();
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  if (success) {
    return (
      <div className="container section" style={{ textAlign: "center" }}>
        <div className="alert alert-success" style={{ fontSize: "1.2rem", maxWidth: 500, margin: "3rem auto" }}>
          {t.order_success}
        </div>
        <Link href="/catalog" className="btn btn-primary">{t.continue_shopping}</Link>
      </div>
    );
  }

  if (items.length === 0) {
    return (
      <div className="container section" style={{ textAlign: "center" }}>
        <p style={{ color: "#6b7280", marginBottom: "1.5rem" }}>{t.empty_cart}</p>
        <Link href="/catalog" className="btn btn-primary">{t.continue_shopping}</Link>
      </div>
    );
  }

  return (
    <>
      <Head><title>{t.checkout}</title></Head>
      <div className="container section">
        <h1 className="section-title">{t.checkout}</h1>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "2rem" }}>
          {/* Form */}
          <form onSubmit={handleSubmit}>
            {error && <div className="alert alert-error">{error}</div>}

            <div className="form-group">
              <label className="form-label">{t.your_name} *</label>
              <input className="form-input" name="customer_name" value={form.customer_name} onChange={handleChange} required />
            </div>
            <div className="form-group">
              <label className="form-label">{t.email}</label>
              <input className="form-input" name="customer_email" type="email" value={form.customer_email} onChange={handleChange} />
            </div>
            <div className="form-group">
              <label className="form-label">{t.phone}</label>
              <input className="form-input" name="customer_phone" value={form.customer_phone} onChange={handleChange} />
            </div>
            <div className="form-group">
              <label className="form-label">{t.address}</label>
              <textarea className="form-input" name="customer_address" rows={3} value={form.customer_address} onChange={handleChange} />
            </div>
            <div className="form-group">
              <label className="form-label">Note</label>
              <textarea className="form-input" name="note" rows={2} value={form.note} onChange={handleChange} />
            </div>

            <button className="btn btn-primary btn-block" type="submit" disabled={loading}>
              {loading ? "..." : t.place_order}
            </button>
          </form>

          {/* Order summary */}
          <div>
            <h3 style={{ marginBottom: "1rem" }}>{t.order}</h3>
            {items.map((item) => (
              <div key={item.id} style={{ display: "flex", justifyContent: "space-between", padding: "0.5rem 0", borderBottom: "1px solid #e5e7eb" }}>
                <span>{item.name} x{item.qty}</span>
                <span style={{ fontWeight: 600 }}>${(item.price * item.qty).toFixed(2)}</span>
              </div>
            ))}
            <div style={{ display: "flex", justifyContent: "space-between", padding: "1rem 0", fontSize: "1.25rem", fontWeight: 700 }}>
              <span>{t.total}</span>
              <span>${total.toFixed(2)}</span>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
