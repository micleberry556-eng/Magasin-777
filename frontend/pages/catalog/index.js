/**
 * Catalog page — product listing with category filter and search.
 */
import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import Head from "next/head";
import Link from "next/link";
import ProductCard from "../../components/ProductCard";
import { useLang } from "../../lib/useLang";

export default function Catalog() {
  const { t } = useLang();
  const router = useRouter();
  const { category: catSlug, search: searchQuery } = router.query;

  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [search, setSearch] = useState("");
  const [activeCat, setActiveCat] = useState(null);

  useEffect(() => {
    fetch("/api/categories").then((r) => r.json()).then(setCategories).catch(() => {});
  }, []);

  useEffect(() => {
    if (catSlug) {
      fetch("/api/categories")
        .then((r) => r.json())
        .then((cats) => {
          const found = cats.find((c) => c.slug === catSlug);
          if (found) setActiveCat(found.id);
        })
        .catch(() => {});
    }
    if (searchQuery) setSearch(searchQuery);
  }, [catSlug, searchQuery]);

  useEffect(() => {
    let url = "/api/products?limit=100";
    if (activeCat) url += `&category_id=${activeCat}`;
    if (search) url += `&search=${encodeURIComponent(search)}`;
    fetch(url).then((r) => r.json()).then(setProducts).catch(() => {});
  }, [activeCat, search]);

  return (
    <>
      <Head><title>{t.catalog}</title></Head>
      <div className="container">
        <div className="breadcrumb">
          <Link href="/">{t.home}</Link> / <span>{t.catalog}</span>
        </div>

        {/* Search */}
        <div style={{ marginBottom: "1.5rem" }}>
          <input
            className="form-input"
            placeholder={t.search + "..."}
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{ maxWidth: 400 }}
          />
        </div>

        {/* Category filter */}
        <div className="cat-pills">
          <span
            className={`cat-pill ${!activeCat ? "active" : ""}`}
            onClick={() => setActiveCat(null)}
          >
            {t.all_categories}
          </span>
          {categories.map((cat) => (
            <span
              key={cat.id}
              className={`cat-pill ${activeCat === cat.id ? "active" : ""}`}
              onClick={() => setActiveCat(activeCat === cat.id ? null : cat.id)}
            >
              {cat.name}
            </span>
          ))}
        </div>

        {/* Products */}
        <div className="product-grid">
          {products.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
        </div>
        {products.length === 0 && (
          <p style={{ textAlign: "center", color: "#6b7280", padding: "3rem 0" }}>
            {t.products}: 0
          </p>
        )}
      </div>
    </>
  );
}
