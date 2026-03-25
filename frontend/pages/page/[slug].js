/**
 * CMS page display.
 */
import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import Head from "next/head";
import Link from "next/link";
import { useLang } from "../../lib/useLang";

export default function CmsPage() {
  const router = useRouter();
  const { slug } = router.query;
  const { t } = useLang();
  const [page, setPage] = useState(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    if (!slug) return;
    fetch(`/api/pages/${slug}`)
      .then((r) => {
        if (!r.ok) throw new Error("Not found");
        return r.json();
      })
      .then(setPage)
      .catch(() => setError(true));
  }, [slug]);

  if (error) {
    return (
      <div className="container section" style={{ textAlign: "center" }}>
        <h1>404</h1>
        <p>Page not found</p>
        <Link href="/" className="btn btn-primary" style={{ marginTop: "1rem" }}>{t.home}</Link>
      </div>
    );
  }

  if (!page) {
    return <div className="container section">Loading...</div>;
  }

  return (
    <>
      <Head>
        <title>{page.seo_title || page.title}</title>
        {page.seo_description && <meta name="description" content={page.seo_description} />}
      </Head>
      <div className="container section">
        <div className="breadcrumb">
          <Link href="/">{t.home}</Link> / <span>{page.title}</span>
        </div>
        <h1 className="section-title">{page.title}</h1>
        <div
          style={{ lineHeight: 1.8, maxWidth: 800 }}
          dangerouslySetInnerHTML={{ __html: page.content }}
        />
      </div>
    </>
  );
}
