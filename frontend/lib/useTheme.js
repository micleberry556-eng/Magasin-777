/**
 * Theme context — loads active theme from site settings and applies CSS variables.
 */
import { createContext, useContext, useState, useEffect } from "react";

const ThemeContext = createContext(null);

const DEFAULT_THEME = {
  primary_color: "#2563eb", secondary_color: "#7c3aed", accent_color: "#f59e0b",
  bg_color: "#ffffff", text_color: "#111827", card_bg: "#f9fafb",
  header_bg: "#1f2937", header_text: "#ffffff", footer_bg: "#111827",
  footer_text: "#d1d5db", font_family: "Inter", heading_font: "Inter",
  font_size_base: "16px", border_radius: "8px", layout_style: "modern",
};

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState(DEFAULT_THEME);
  const [settings, setSettings] = useState(null);

  useEffect(() => {
    fetch("/api/settings")
      .then((r) => r.json())
      .then((s) => {
        setSettings(s);
        if (s.active_theme_id) {
          fetch(`/api/themes/${s.active_theme_id}`)
            .then((r) => r.json())
            .then((t) => setTheme(t))
            .catch(() => {});
        }
      })
      .catch(() => {});
  }, []);

  // Apply CSS variables to document root
  useEffect(() => {
    if (typeof document === "undefined") return;
    const root = document.documentElement.style;
    root.setProperty("--color-primary", theme.primary_color);
    root.setProperty("--color-secondary", theme.secondary_color);
    root.setProperty("--color-accent", theme.accent_color);
    root.setProperty("--color-bg", theme.bg_color);
    root.setProperty("--color-text", theme.text_color);
    root.setProperty("--color-card", theme.card_bg);
    root.setProperty("--color-header-bg", theme.header_bg);
    root.setProperty("--color-header-text", theme.header_text);
    root.setProperty("--color-footer-bg", theme.footer_bg);
    root.setProperty("--color-footer-text", theme.footer_text);
    root.setProperty("--font-family", theme.font_family + ", sans-serif");
    root.setProperty("--font-heading", theme.heading_font + ", sans-serif");
    root.setProperty("--font-size-base", theme.font_size_base);
    root.setProperty("--border-radius", theme.border_radius);
  }, [theme]);

  return (
    <ThemeContext.Provider value={{ theme, settings, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within ThemeProvider");
  return ctx;
}
