/**
 * Language context — fetches translations from backend API.
 */
import { createContext, useContext, useState, useEffect, useCallback } from "react";

const LangContext = createContext(null);

const FALLBACK = {
  home: "Home", catalog: "Catalog", cart: "Cart", checkout: "Checkout",
  search: "Search", categories: "Categories", products: "Products",
  price: "Price", add_to_cart: "Add to Cart", buy_now: "Buy Now",
  description: "Description", reviews: "Reviews", in_stock: "In Stock",
  out_of_stock: "Out of Stock", total: "Total", order: "Order",
  your_name: "Your Name", email: "Email", phone: "Phone", address: "Address",
  place_order: "Place Order", order_success: "Order placed successfully!",
  continue_shopping: "Continue Shopping", empty_cart: "Your cart is empty",
  about: "About", contacts: "Contacts", all_categories: "All Categories",
  featured: "Featured", new_arrivals: "New Arrivals", sale: "Sale",
  quantity: "Quantity", remove: "Remove", language: "Language",
  currency: "Currency", footer_text: "All rights reserved",
};

export function LangProvider({ children }) {
  const [lang, setLangState] = useState("ru");
  const [t, setT] = useState(FALLBACK);
  const [languages, setLanguages] = useState([]);

  useEffect(() => {
    try {
      const saved = localStorage.getItem("lm_lang");
      if (saved) setLangState(saved);
    } catch {}
    fetch("/api/i18n")
      .then((r) => r.json())
      .then((data) => {
        setLanguages(
          data.languages.map((code) => ({ code, name: data.names[code] || code }))
        );
      })
      .catch(() => {});
  }, []);

  useEffect(() => {
    fetch(`/api/i18n/${lang}`)
      .then((r) => r.json())
      .then((data) => setT(data.translations || FALLBACK))
      .catch(() => setT(FALLBACK));
  }, [lang]);

  const setLang = useCallback((code) => {
    setLangState(code);
    try { localStorage.setItem("lm_lang", code); } catch {}
  }, []);

  return (
    <LangContext.Provider value={{ lang, setLang, t, languages }}>
      {children}
    </LangContext.Provider>
  );
}

export function useLang() {
  const ctx = useContext(LangContext);
  if (!ctx) throw new Error("useLang must be used within LangProvider");
  return ctx;
}
