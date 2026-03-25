"""Generate 300 unique themes across multiple categories and styles."""

from typing import Any

# Google Fonts that are widely available
FONTS = [
    "Inter", "Roboto", "Open Sans", "Montserrat", "Lato", "Poppins",
    "Nunito", "Raleway", "Ubuntu", "Merriweather", "Playfair Display",
    "Source Sans 3", "Oswald", "Noto Sans", "PT Sans", "Rubik",
    "Work Sans", "Fira Sans", "Quicksand", "Mulish",
]

HEADING_FONTS = [
    "Inter", "Montserrat", "Playfair Display", "Oswald", "Raleway",
    "Poppins", "Merriweather", "Roboto Slab", "Lora", "Nunito",
]

LAYOUTS = ["modern", "classic", "minimal", "bold"]
RADII = ["0px", "4px", "8px", "12px", "16px", "24px", "9999px"]

# Theme category definitions with base palettes
CATEGORIES: dict[str, list[dict[str, str]]] = {
    "light": [
        {"primary": "#2563eb", "secondary": "#7c3aed", "accent": "#f59e0b", "bg": "#ffffff", "text": "#111827", "card": "#f9fafb", "header_bg": "#ffffff", "header_text": "#111827", "footer_bg": "#f3f4f6", "footer_text": "#6b7280"},
        {"primary": "#0891b2", "secondary": "#6366f1", "accent": "#f97316", "bg": "#fefefe", "text": "#1e293b", "card": "#f8fafc", "header_bg": "#f0f9ff", "header_text": "#0c4a6e", "footer_bg": "#e0f2fe", "footer_text": "#075985"},
        {"primary": "#059669", "secondary": "#8b5cf6", "accent": "#eab308", "bg": "#ffffff", "text": "#1f2937", "card": "#f0fdf4", "header_bg": "#ecfdf5", "header_text": "#065f46", "footer_bg": "#d1fae5", "footer_text": "#047857"},
        {"primary": "#dc2626", "secondary": "#4f46e5", "accent": "#fbbf24", "bg": "#ffffff", "text": "#18181b", "card": "#fef2f2", "header_bg": "#fff7ed", "header_text": "#9a3412", "footer_bg": "#fef3c7", "footer_text": "#92400e"},
        {"primary": "#7c3aed", "secondary": "#ec4899", "accent": "#14b8a6", "bg": "#faf5ff", "text": "#1e1b4b", "card": "#f5f3ff", "header_bg": "#ede9fe", "header_text": "#5b21b6", "footer_bg": "#ddd6fe", "footer_text": "#6d28d9"},
    ],
    "dark": [
        {"primary": "#3b82f6", "secondary": "#a78bfa", "accent": "#fbbf24", "bg": "#0f172a", "text": "#e2e8f0", "card": "#1e293b", "header_bg": "#020617", "header_text": "#f1f5f9", "footer_bg": "#020617", "footer_text": "#94a3b8"},
        {"primary": "#22d3ee", "secondary": "#818cf8", "accent": "#fb923c", "bg": "#111827", "text": "#f3f4f6", "card": "#1f2937", "header_bg": "#030712", "header_text": "#e5e7eb", "footer_bg": "#030712", "footer_text": "#9ca3af"},
        {"primary": "#34d399", "secondary": "#c084fc", "accent": "#facc15", "bg": "#0c0a09", "text": "#fafaf9", "card": "#1c1917", "header_bg": "#0a0a0a", "header_text": "#f5f5f4", "footer_bg": "#0a0a0a", "footer_text": "#a8a29e"},
        {"primary": "#f43f5e", "secondary": "#a855f7", "accent": "#38bdf8", "bg": "#18181b", "text": "#fafafa", "card": "#27272a", "header_bg": "#09090b", "header_text": "#f4f4f5", "footer_bg": "#09090b", "footer_text": "#a1a1aa"},
        {"primary": "#e879f9", "secondary": "#67e8f9", "accent": "#a3e635", "bg": "#1a1a2e", "text": "#eef2ff", "card": "#16213e", "header_bg": "#0f0f23", "header_text": "#c7d2fe", "footer_bg": "#0f0f23", "footer_text": "#818cf8"},
    ],
    "colorful": [
        {"primary": "#e11d48", "secondary": "#7c3aed", "accent": "#06b6d4", "bg": "#fff1f2", "text": "#1f2937", "card": "#ffe4e6", "header_bg": "#be123c", "header_text": "#ffffff", "footer_bg": "#9f1239", "footer_text": "#fecdd3"},
        {"primary": "#2563eb", "secondary": "#f97316", "accent": "#10b981", "bg": "#eff6ff", "text": "#1e3a5f", "card": "#dbeafe", "header_bg": "#1d4ed8", "header_text": "#ffffff", "footer_bg": "#1e40af", "footer_text": "#bfdbfe"},
        {"primary": "#16a34a", "secondary": "#eab308", "accent": "#e11d48", "bg": "#f0fdf4", "text": "#14532d", "card": "#dcfce7", "header_bg": "#15803d", "header_text": "#ffffff", "footer_bg": "#166534", "footer_text": "#bbf7d0"},
        {"primary": "#9333ea", "secondary": "#f43f5e", "accent": "#06b6d4", "bg": "#faf5ff", "text": "#3b0764", "card": "#f3e8ff", "header_bg": "#7e22ce", "header_text": "#ffffff", "footer_bg": "#6b21a8", "footer_text": "#d8b4fe"},
        {"primary": "#ea580c", "secondary": "#0284c7", "accent": "#65a30d", "bg": "#fff7ed", "text": "#431407", "card": "#ffedd5", "header_bg": "#c2410c", "header_text": "#ffffff", "footer_bg": "#9a3412", "footer_text": "#fed7aa"},
    ],
    "minimal": [
        {"primary": "#374151", "secondary": "#6b7280", "accent": "#111827", "bg": "#ffffff", "text": "#111827", "card": "#f9fafb", "header_bg": "#ffffff", "header_text": "#111827", "footer_bg": "#f9fafb", "footer_text": "#6b7280"},
        {"primary": "#1f2937", "secondary": "#9ca3af", "accent": "#374151", "bg": "#fafafa", "text": "#171717", "card": "#f5f5f5", "header_bg": "#fafafa", "header_text": "#171717", "footer_bg": "#f5f5f5", "footer_text": "#737373"},
        {"primary": "#0f172a", "secondary": "#64748b", "accent": "#334155", "bg": "#f8fafc", "text": "#0f172a", "card": "#f1f5f9", "header_bg": "#f8fafc", "header_text": "#0f172a", "footer_bg": "#f1f5f9", "footer_text": "#64748b"},
        {"primary": "#292524", "secondary": "#a8a29e", "accent": "#57534e", "bg": "#fafaf9", "text": "#1c1917", "card": "#f5f5f4", "header_bg": "#fafaf9", "header_text": "#1c1917", "footer_bg": "#f5f5f4", "footer_text": "#78716c"},
        {"primary": "#18181b", "secondary": "#a1a1aa", "accent": "#3f3f46", "bg": "#ffffff", "text": "#18181b", "card": "#fafafa", "header_bg": "#ffffff", "header_text": "#18181b", "footer_bg": "#fafafa", "footer_text": "#71717a"},
    ],
    "neon": [
        {"primary": "#00ff88", "secondary": "#ff00ff", "accent": "#00ffff", "bg": "#0a0a0a", "text": "#00ff88", "card": "#1a1a1a", "header_bg": "#0a0a0a", "header_text": "#00ff88", "footer_bg": "#050505", "footer_text": "#00ff88"},
        {"primary": "#ff3366", "secondary": "#33ccff", "accent": "#ffff00", "bg": "#0d0d0d", "text": "#ff3366", "card": "#1a1a2e", "header_bg": "#0d0d0d", "header_text": "#ff3366", "footer_bg": "#050510", "footer_text": "#ff3366"},
        {"primary": "#bf00ff", "secondary": "#00ffcc", "accent": "#ff6600", "bg": "#0a000f", "text": "#e0b0ff", "card": "#1a0a2e", "header_bg": "#0a000f", "header_text": "#bf00ff", "footer_bg": "#050008", "footer_text": "#bf00ff"},
        {"primary": "#39ff14", "secondary": "#ff073a", "accent": "#00e5ff", "bg": "#0b0b0b", "text": "#39ff14", "card": "#151515", "header_bg": "#0b0b0b", "header_text": "#39ff14", "footer_bg": "#050505", "footer_text": "#39ff14"},
        {"primary": "#fe019a", "secondary": "#04d9ff", "accent": "#ccff00", "bg": "#0e0e10", "text": "#f0f0f0", "card": "#1c1c20", "header_bg": "#0e0e10", "header_text": "#fe019a", "footer_bg": "#08080a", "footer_text": "#fe019a"},
    ],
    "pastel": [
        {"primary": "#93c5fd", "secondary": "#c4b5fd", "accent": "#fcd34d", "bg": "#f0f9ff", "text": "#1e3a5f", "card": "#e0f2fe", "header_bg": "#dbeafe", "header_text": "#1e40af", "footer_bg": "#bfdbfe", "footer_text": "#1d4ed8"},
        {"primary": "#86efac", "secondary": "#fda4af", "accent": "#fde68a", "bg": "#f0fdf4", "text": "#14532d", "card": "#dcfce7", "header_bg": "#bbf7d0", "header_text": "#166534", "footer_bg": "#a7f3d0", "footer_text": "#15803d"},
        {"primary": "#fda4af", "secondary": "#a5b4fc", "accent": "#99f6e4", "bg": "#fff1f2", "text": "#4c0519", "card": "#ffe4e6", "header_bg": "#fecdd3", "header_text": "#9f1239", "footer_bg": "#fda4af", "footer_text": "#be123c"},
        {"primary": "#c4b5fd", "secondary": "#fbcfe8", "accent": "#a5f3fc", "bg": "#faf5ff", "text": "#3b0764", "card": "#f3e8ff", "header_bg": "#ede9fe", "header_text": "#6b21a8", "footer_bg": "#ddd6fe", "footer_text": "#7e22ce"},
        {"primary": "#fde68a", "secondary": "#a5b4fc", "accent": "#86efac", "bg": "#fefce8", "text": "#422006", "card": "#fef9c3", "header_bg": "#fef08a", "header_text": "#854d0e", "footer_bg": "#fde047", "footer_text": "#a16207"},
    ],
    "corporate": [
        {"primary": "#1e40af", "secondary": "#1e3a5f", "accent": "#b91c1c", "bg": "#ffffff", "text": "#1f2937", "card": "#f8fafc", "header_bg": "#1e3a8a", "header_text": "#ffffff", "footer_bg": "#1e3a8a", "footer_text": "#bfdbfe"},
        {"primary": "#0f766e", "secondary": "#1e3a5f", "accent": "#b45309", "bg": "#ffffff", "text": "#1f2937", "card": "#f0fdfa", "header_bg": "#134e4a", "header_text": "#ffffff", "footer_bg": "#134e4a", "footer_text": "#99f6e4"},
        {"primary": "#7e22ce", "secondary": "#1e1b4b", "accent": "#ca8a04", "bg": "#faf5ff", "text": "#1e1b4b", "card": "#f5f3ff", "header_bg": "#581c87", "header_text": "#ffffff", "footer_bg": "#3b0764", "footer_text": "#d8b4fe"},
        {"primary": "#0369a1", "secondary": "#0c4a6e", "accent": "#dc2626", "bg": "#f0f9ff", "text": "#0c4a6e", "card": "#e0f2fe", "header_bg": "#075985", "header_text": "#ffffff", "footer_bg": "#0c4a6e", "footer_text": "#7dd3fc"},
        {"primary": "#4338ca", "secondary": "#312e81", "accent": "#ea580c", "bg": "#eef2ff", "text": "#312e81", "card": "#e0e7ff", "header_bg": "#3730a3", "header_text": "#ffffff", "footer_bg": "#312e81", "footer_text": "#a5b4fc"},
    ],
    "gradient": [
        {"primary": "#6366f1", "secondary": "#ec4899", "accent": "#f59e0b", "bg": "#fdf2f8", "text": "#1e1b4b", "card": "#fce7f3", "header_bg": "#4f46e5", "header_text": "#ffffff", "footer_bg": "#3730a3", "footer_text": "#c7d2fe"},
        {"primary": "#06b6d4", "secondary": "#8b5cf6", "accent": "#f97316", "bg": "#ecfeff", "text": "#164e63", "card": "#cffafe", "header_bg": "#0891b2", "header_text": "#ffffff", "footer_bg": "#0e7490", "footer_text": "#a5f3fc"},
        {"primary": "#f43f5e", "secondary": "#f97316", "accent": "#14b8a6", "bg": "#fff1f2", "text": "#4c0519", "card": "#ffe4e6", "header_bg": "#e11d48", "header_text": "#ffffff", "footer_bg": "#be123c", "footer_text": "#fecdd3"},
        {"primary": "#10b981", "secondary": "#3b82f6", "accent": "#f59e0b", "bg": "#ecfdf5", "text": "#064e3b", "card": "#d1fae5", "header_bg": "#059669", "header_text": "#ffffff", "footer_bg": "#047857", "footer_text": "#a7f3d0"},
        {"primary": "#8b5cf6", "secondary": "#06b6d4", "accent": "#f43f5e", "bg": "#f5f3ff", "text": "#2e1065", "card": "#ede9fe", "header_bg": "#7c3aed", "header_text": "#ffffff", "footer_bg": "#6d28d9", "footer_text": "#c4b5fd"},
    ],
}

# Category display names
CATEGORY_NAMES = {
    "light": "Светлые",
    "dark": "Тёмные",
    "colorful": "Яркие",
    "minimal": "Минималистичные",
    "neon": "Неоновые",
    "pastel": "Пастельные",
    "corporate": "Корпоративные",
    "gradient": "Градиентные",
}


def generate_all_themes() -> list[dict[str, Any]]:
    """Generate 300 themes by combining palettes, fonts, layouts, and radii."""
    themes: list[dict[str, Any]] = []
    theme_id = 0

    for cat_key, palettes in CATEGORIES.items():
        # Each category gets ~37-38 themes to reach 300 total
        variations_per_palette = 8  # 8 categories * 5 palettes * ~8 = 320, we trim to 300
        for p_idx, palette in enumerate(palettes):
            for v in range(variations_per_palette):
                if theme_id >= 300:
                    return themes

                font_idx = (theme_id + v) % len(FONTS)
                heading_idx = (theme_id + v + 3) % len(HEADING_FONTS)
                layout_idx = v % len(LAYOUTS)
                radius_idx = (v + p_idx) % len(RADII)

                cat_display = CATEGORY_NAMES.get(cat_key, cat_key.title())
                name = f"{cat_display} #{p_idx + 1}.{v + 1}"
                slug = f"{cat_key}-{p_idx + 1}-{v + 1}"

                themes.append({
                    "name": name,
                    "slug": slug,
                    "primary_color": palette["primary"],
                    "secondary_color": palette["secondary"],
                    "accent_color": palette["accent"],
                    "bg_color": palette["bg"],
                    "text_color": palette["text"],
                    "card_bg": palette["card"],
                    "header_bg": palette["header_bg"],
                    "header_text": palette["header_text"],
                    "footer_bg": palette["footer_bg"],
                    "footer_text": palette["footer_text"],
                    "font_family": FONTS[font_idx],
                    "heading_font": HEADING_FONTS[heading_idx],
                    "font_size_base": "16px",
                    "border_radius": RADII[radius_idx],
                    "layout_style": LAYOUTS[layout_idx],
                    "preview_url": "",
                    "category": cat_key,
                })
                theme_id += 1

    return themes
