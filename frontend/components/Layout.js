/**
 * Main layout — header, content, footer.
 */
import Link from "next/link";
import { useCart } from "../lib/useCart";
import { useLang } from "../lib/useLang";
import { useTheme } from "../lib/useTheme";

export default function Layout({ children }) {
  const { count } = useCart();
  const { t, lang, setLang, languages } = useLang();
  const { settings } = useTheme();

  const siteName = settings?.site_name || "LocalMarket";

  return (
    <>
      <header className="header">
        <div className="container header-inner">
          <Link href="/" className="header-logo">{siteName}</Link>
          <nav className="header-nav">
            <Link href="/">{t.home}</Link>
            <Link href="/catalog">{t.catalog}</Link>
            <Link href="/cart">
              <span className="cart-badge">
                {t.cart}
                {count > 0 && <span className="count">{count}</span>}
              </span>
            </Link>
            <select
              className="lang-select"
              value={lang}
              onChange={(e) => setLang(e.target.value)}
              aria-label={t.language}
            >
              {languages.map((l) => (
                <option key={l.code} value={l.code}>{l.name}</option>
              ))}
            </select>
          </nav>
        </div>
      </header>

      <main style={{ minHeight: "60vh" }}>{children}</main>

      <footer className="footer">
        <div className="container footer-inner">
          <div>&copy; {new Date().getFullYear()} {siteName}. {t.footer_text}.</div>
          <nav style={{ display: "flex", gap: "1rem" }}>
            <Link href="/page/about">{t.about}</Link>
            <Link href="/page/contacts">{t.contacts}</Link>
          </nav>
        </div>
      </footer>
    </>
  );
}
