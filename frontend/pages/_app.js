/**
 * Next.js App wrapper — providers for cart, language, theme.
 */
import { CartProvider } from "../lib/useCart";
import { LangProvider } from "../lib/useLang";
import { ThemeProvider } from "../lib/useTheme";
import Layout from "../components/Layout";
import "../styles/globals.css";
import "../styles/admin.css";

export default function App({ Component, pageProps }) {
  // Admin pages don't use the store layout
  const isAdmin = Component.isAdmin;

  return (
    <LangProvider>
      <ThemeProvider>
        <CartProvider>
          {isAdmin ? (
            <Component {...pageProps} />
          ) : (
            <Layout>
              <Component {...pageProps} />
            </Layout>
          )}
        </CartProvider>
      </ThemeProvider>
    </LangProvider>
  );
}
