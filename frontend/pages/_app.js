/**
 * Next.js App wrapper — providers for cart, language, theme, admin.
 * AdminProvider is ALWAYS mounted to preserve auth state across page transitions.
 */
import { CartProvider } from "../lib/useCart";
import { LangProvider } from "../lib/useLang";
import { ThemeProvider } from "../lib/useTheme";
import { AdminProvider } from "../lib/useAdmin";
import Layout from "../components/Layout";
import "../styles/globals.css";
import "../styles/admin.css";

export default function App({ Component, pageProps }) {
  const isAdmin = Component.isAdmin;

  return (
    <AdminProvider>
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
    </AdminProvider>
  );
}
