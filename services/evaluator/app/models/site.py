"""Site settings, pages, and theme models."""

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class SiteSettings(Base):
    """Global site configuration — single row table."""

    __tablename__ = "site_settings"

    id: Mapped[int] = mapped_column(primary_key=True)
    site_name: Mapped[str] = mapped_column(String(255), default="LocalMarket")
    site_description: Mapped[str] = mapped_column(String(500), default="")
    logo_url: Mapped[str] = mapped_column(String(500), default="")
    favicon_url: Mapped[str] = mapped_column(String(500), default="")
    background_url: Mapped[str] = mapped_column(String(500), default="")
    currency: Mapped[str] = mapped_column(String(10), default="USD")
    default_language: Mapped[str] = mapped_column(String(10), default="ru")
    active_theme_id: Mapped[int] = mapped_column(Integer, default=1)
    # SEO defaults
    seo_title: Mapped[str] = mapped_column(String(255), default="")
    seo_description: Mapped[str] = mapped_column(String(500), default="")
    seo_keywords: Mapped[str] = mapped_column(String(500), default="")
    # Contact
    contact_email: Mapped[str] = mapped_column(String(255), default="")
    contact_phone: Mapped[str] = mapped_column(String(50), default="")
    contact_address: Mapped[str] = mapped_column(Text, default="")
    # Social
    social_links: Mapped[str] = mapped_column(Text, default="{}")  # JSON
    # Analytics
    analytics_code: Mapped[str] = mapped_column(Text, default="")


class Page(Base):
    """CMS pages editable from admin panel."""

    __tablename__ = "pages"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    content: Mapped[str] = mapped_column(Text, default="")
    is_published: Mapped[bool] = mapped_column(Boolean, default=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0)
    seo_title: Mapped[str] = mapped_column(String(255), default="")
    seo_description: Mapped[str] = mapped_column(String(500), default="")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


class Theme(Base):
    """Visual theme definition."""

    __tablename__ = "themes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    # Colors
    primary_color: Mapped[str] = mapped_column(String(20), default="#2563eb")
    secondary_color: Mapped[str] = mapped_column(String(20), default="#7c3aed")
    accent_color: Mapped[str] = mapped_column(String(20), default="#f59e0b")
    bg_color: Mapped[str] = mapped_column(String(20), default="#ffffff")
    text_color: Mapped[str] = mapped_column(String(20), default="#111827")
    card_bg: Mapped[str] = mapped_column(String(20), default="#f9fafb")
    header_bg: Mapped[str] = mapped_column(String(20), default="#1f2937")
    header_text: Mapped[str] = mapped_column(String(20), default="#ffffff")
    footer_bg: Mapped[str] = mapped_column(String(20), default="#111827")
    footer_text: Mapped[str] = mapped_column(String(20), default="#d1d5db")
    # Typography
    font_family: Mapped[str] = mapped_column(String(100), default="Inter")
    heading_font: Mapped[str] = mapped_column(String(100), default="Inter")
    font_size_base: Mapped[str] = mapped_column(String(10), default="16px")
    # Layout
    border_radius: Mapped[str] = mapped_column(String(10), default="8px")
    layout_style: Mapped[str] = mapped_column(String(50), default="modern")  # modern, classic, minimal, bold
    # Preview
    preview_url: Mapped[str] = mapped_column(String(500), default="")
    category: Mapped[str] = mapped_column(String(50), default="general")  # general, dark, light, colorful, minimal, neon, pastel, corporate
