/**
 * Cart page.
 */
import Head from "next/head";
import Link from "next/link";
import { useCart } from "../../lib/useCart";
import { useLang } from "../../lib/useLang";

export default function Cart() {
  const { items, updateQty, removeItem, total, count } = useCart();
  const { t } = useLang();

  return (
    <>
      <Head><title>{t.cart}</title></Head>
      <div className="container section">
        <h1 className="section-title">{t.cart}</h1>

        {items.length === 0 ? (
          <div style={{ textAlign: "center", padding: "3rem 0" }}>
            <p style={{ fontSize: "1.2rem", color: "#6b7280", marginBottom: "1.5rem" }}>{t.empty_cart}</p>
            <Link href="/catalog" className="btn btn-primary">{t.continue_shopping}</Link>
          </div>
        ) : (
          <>
            <table className="cart-table">
              <thead>
                <tr>
                  <th>{t.products}</th>
                  <th>{t.price}</th>
                  <th>{t.quantity}</th>
                  <th>{t.total}</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {items.map((item) => (
                  <tr key={item.id}>
                    <td>
                      <Link href={`/catalog/${item.slug}`} style={{ fontWeight: 500 }}>
                        {item.name}
                      </Link>
                    </td>
                    <td>${item.price}</td>
                    <td>
                      <input
                        type="number"
                        className="qty-input"
                        min={1}
                        value={item.qty}
                        onChange={(e) => updateQty(item.id, parseInt(e.target.value) || 1)}
                      />
                    </td>
                    <td style={{ fontWeight: 600 }}>${(item.price * item.qty).toFixed(2)}</td>
                    <td>
                      <button
                        className="btn btn-outline btn-sm"
                        onClick={() => removeItem(item.id)}
                      >
                        {t.remove}
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>

            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: "2rem", flexWrap: "wrap", gap: "1rem" }}>
              <div style={{ fontSize: "1.5rem", fontWeight: 700 }}>
                {t.total}: ${total.toFixed(2)}
              </div>
              <Link href="/checkout" className="btn btn-primary" style={{ textDecoration: "none" }}>
                {t.checkout}
              </Link>
            </div>
          </>
        )}
      </div>
    </>
  );
}
