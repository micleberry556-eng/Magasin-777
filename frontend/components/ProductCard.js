/**
 * Product card component for grid display.
 */
import Link from "next/link";
import { useCart } from "../lib/useCart";
import { useLang } from "../lib/useLang";

export default function ProductCard({ product }) {
  const { addItem } = useCart();
  const { t } = useLang();

  const imgSrc = product.image || "/placeholder.svg";

  return (
    <div className="card">
      <Link href={`/catalog/${product.slug}`}>
        <img className="card-img" src={imgSrc} alt={product.name} />
      </Link>
      <div className="card-body">
        <Link href={`/catalog/${product.slug}`}>
          <div className="card-title">{product.name}</div>
        </Link>
        <div style={{ marginBottom: "0.75rem" }}>
          <span className="card-price">${product.price}</span>
          {product.old_price && (
            <span className="card-old-price">${product.old_price}</span>
          )}
        </div>
        <button
          className="btn btn-primary btn-sm btn-block"
          onClick={() => addItem(product)}
        >
          {t.add_to_cart}
        </button>
      </div>
    </div>
  );
}
