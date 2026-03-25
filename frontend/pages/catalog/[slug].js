/**
 * Product detail page.
 */
import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import Head from "next/head";
import Link from "next/link";
import { useCart } from "../../lib/useCart";
import { useLang } from "../../lib/useLang";

export default function ProductDetail() {
  const router = useRouter();
  const { slug } = router.query;
  const { addItem } = useCart();
  const { t } = useLang();
  const [product, setProduct] = useState(null);
  const [qty, setQty] = useState(1);
  const [added, setAdded] = useState(false);

  useEffect(() => {
    if (!slug) return;
    fetch(`/api/products/${slug}`)
      .then((r) => r.json())
      .then(setProduct)
      .catch(() => {});
  }, [slug]);

  if (!product) {
    return <div className="container" style={{ padding: "3rem 0", textAlign: "center" }}>Loading...</div>;
  }

  const handleAdd = () => {
    addItem(product, qty);
    setAdded(true);
    setTimeout(() => setAdded(false), 2000);
  };

  return (
    <>
      <Head>
        <title>{product.seo_title || product.name}</title>
        <meta name="description" content={product.seo_description || product.description?.slice(0, 160)} />
      </Head>
      <div className="container">
        <div className="breadcrumb">
          <Link href="/">{t.home}</Link> / <Link href="/catalog">{t.catalog}</Link> / <span>{product.name}</span>
        </div>

        <div className="product-detail">
          <div>
            <img
              className="product-detail-img"
              src={product.image || "/placeholder.svg"}
              alt={product.name}
            />
          </div>
          <div className="product-detail-info">
            <h1>{product.name}</h1>
            {product.sku && (
              <p style={{ color: "#6b7280", fontSize: "0.85rem" }}>SKU: {product.sku}</p>
            )}
            <div className="product-detail-price">
              ${product.price}
              {product.old_price && (
                <span className="product-detail-old-price">${product.old_price}</span>
              )}
            </div>
            <div className="product-detail-stock">
              {product.stock > 0 ? (
                <span className="stock-ok">{t.in_stock} ({product.stock})</span>
              ) : (
                <span className="stock-out">{t.out_of_stock}</span>
              )}
            </div>

            {product.stock > 0 && (
              <div style={{ display: "flex", gap: "0.75rem", alignItems: "center", marginBottom: "1.5rem" }}>
                <label>{t.quantity}:</label>
                <input
                  type="number"
                  className="qty-input"
                  min={1}
                  max={product.stock}
                  value={qty}
                  onChange={(e) => setQty(Math.max(1, parseInt(e.target.value) || 1))}
                />
                <button className="btn btn-primary" onClick={handleAdd}>
                  {t.add_to_cart}
                </button>
              </div>
            )}

            {added && <div className="alert alert-success">{t.add_to_cart} ✓</div>}

            <h3>{t.description}</h3>
            <p style={{ whiteSpace: "pre-wrap" }}>{product.description}</p>
          </div>
        </div>
      </div>
    </>
  );
}
