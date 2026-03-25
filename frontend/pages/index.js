/**
 * Home page — hero + featured products + categories.
 */
import { useState, useEffect } from "react";
import Head from "next/head";
import Link from "next/link";
import ProductCard from "../components/ProductCard";
import { useLang } from "../lib/useLang";
import { useTheme } from "../lib/useTheme";

export default function Home() {
  const { t } = useLang();
  const { settings } = useTheme();
  const [featured, setFeatured] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetch("/api/products?featured=true&limit=8")
      .then((r) => r.json())
      .then(setFeatured)
      .catch(() => {});
    fetch("/api/categories")
      .then((r) => r.json())
      .then(setCategories)
      .catch(() => {});
  }, []);

  const seoTitle = settings?.seo_title || settings?.site_name || "LocalMarket";
  const seoDesc = settings?.seo_description || "";

  return (
    <>
      <Head>
        <title>{seoTitle}</title>
        <meta name="description" content={seoDesc} />
        {settings?.seo_keywords && (
          <meta name="keywords" content={settings.seo_keywords} />
        )}
      </Head>

      {/* Hero */}
      <section
        className="hero"
        style={settings?.background_url ? {
          backgroundImage: `url(${settings.background_url})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
        } : {}}
      >
        <div className="container">
          <h1>{settings?.site_name || "LocalMarket"}</h1>
          <p>{settings?.site_description || t.catalog}</p>
          <div style={{ marginTop: "1.5rem" }}>
            <Link href="/catalog" className="btn btn-accent" style={{ textDecoration: "none" }}>
              {t.catalog}
            </Link>
          </div>
        </div>
      </section>

      {/* Categories */}
      {categories.length > 0 && (
        <section className="section">
          <div className="container">
            <h2 className="section-title">{t.categories}</h2>
            <div className="cat-pills">
              {categories.map((cat) => (
                <Link key={cat.id} href={`/catalog?category=${cat.slug}`}>
                  <span className="cat-pill">{cat.name}</span>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Featured products */}
      {featured.length > 0 && (
        <section className="section">
          <div className="container">
            <h2 className="section-title">{t.featured}</h2>
            <div className="product-grid">
              {featured.map((p) => (
                <ProductCard key={p.id} product={p} />
              ))}
            </div>
          </div>
        </section>
      )}
    </>
  );
}
