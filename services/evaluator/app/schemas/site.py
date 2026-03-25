"""Site settings, page, and theme schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# --- Site Settings ---
class SiteSettingsUpdate(BaseModel):
    site_name: Optional[str] = None
    site_description: Optional[str] = None
    logo_url: Optional[str] = None
    favicon_url: Optional[str] = None
    background_url: Optional[str] = None
    currency: Optional[str] = None
    default_language: Optional[str] = None
    active_theme_id: Optional[int] = None
    seo_title: Optional[str] = None
    seo_description: Optional[str] = None
    seo_keywords: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_address: Optional[str] = None
    social_links: Optional[str] = None
    analytics_code: Optional[str] = None


class SiteSettingsOut(BaseModel):
    id: int
    site_name: str
    site_description: str
    logo_url: str
    favicon_url: str
    background_url: str
    currency: str
    default_language: str
    active_theme_id: int
    seo_title: str
    seo_description: str
    seo_keywords: str
    contact_email: str
    contact_phone: str
    contact_address: str
    social_links: str
    analytics_code: str

    model_config = {"from_attributes": True}


# --- Page ---
class PageCreate(BaseModel):
    title: str
    slug: str
    content: str = ""
    is_published: bool = True
    sort_order: int = 0
    seo_title: str = ""
    seo_description: str = ""


class PageUpdate(BaseModel):
    title: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None
    is_published: Optional[bool] = None
    sort_order: Optional[int] = None
    seo_title: Optional[str] = None
    seo_description: Optional[str] = None


class PageOut(BaseModel):
    id: int
    title: str
    slug: str
    content: str
    is_published: bool
    sort_order: int
    seo_title: str
    seo_description: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# --- Theme ---
class ThemeOut(BaseModel):
    id: int
    name: str
    slug: str
    primary_color: str
    secondary_color: str
    accent_color: str
    bg_color: str
    text_color: str
    card_bg: str
    header_bg: str
    header_text: str
    footer_bg: str
    footer_text: str
    font_family: str
    heading_font: str
    font_size_base: str
    border_radius: str
    layout_style: str
    preview_url: str
    category: str

    model_config = {"from_attributes": True}
