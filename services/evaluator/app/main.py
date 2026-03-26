"""
LocalMarket — Main API Application
====================================
Full-featured e-commerce backend with admin panel support.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import DEFAULT_ADMIN_EMAIL, DEFAULT_ADMIN_PASSWORD, UPLOAD_DIR
from app.core.database import Base, SessionLocal, engine
from app.core.i18n import LANGUAGE_NAMES, SUPPORTED_LANGUAGES, get_translations
from app.core.security import hash_password
from app.models.order import Order, OrderItem  # noqa: F401 — register models
from app.models.product import Category, Product, StockMovement  # noqa: F401
from app.models.site import Page, SiteSettings, Theme  # noqa: F401
from app.models.user import User
from app.routers import admin_auth, categories, orders, pages, products, settings, stock, themes, upload

app = FastAPI(title="LocalMarket API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files for uploads
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory="/app/static"), name="static")

# --- Routers ---
app.include_router(admin_auth.router, prefix="/api/admin", tags=["Admin Auth"])
app.include_router(products.router, prefix="/api", tags=["Products"])
app.include_router(categories.router, prefix="/api", tags=["Categories"])
app.include_router(orders.router, prefix="/api", tags=["Orders"])
app.include_router(pages.router, prefix="/api", tags=["Pages"])
app.include_router(settings.router, prefix="/api", tags=["Settings"])
app.include_router(themes.router, prefix="/api", tags=["Themes"])
app.include_router(stock.router, prefix="/api/admin", tags=["Stock"])
app.include_router(upload.router, prefix="/api/admin", tags=["Upload"])


# --- Startup: seed DB ---
@app.on_event("startup")
def startup_seed():
    """Create tables and seed initial data on first run."""
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        _seed_admin(db)
        _seed_settings(db)
        _seed_themes(db)
        _seed_demo_data(db)
        db.commit()
    finally:
        db.close()


def _seed_admin(db):
    existing = db.query(User).filter(User.email == DEFAULT_ADMIN_EMAIL).first()
    if not existing:
        db.add(
            User(
                email=DEFAULT_ADMIN_EMAIL,
                password_hash=hash_password(DEFAULT_ADMIN_PASSWORD),
                role="admin",
                name="Administrator",
            )
        )
    else:
        # Re-hash password on every startup to fix bcrypt compatibility issues
        existing.password_hash = hash_password(DEFAULT_ADMIN_PASSWORD)
        existing.role = "admin"


def _seed_settings(db):
    existing = db.query(SiteSettings).first()
    if not existing:
        db.add(
            SiteSettings(
                site_name="LocalMarket",
                site_description="Online marketplace",
                default_language="ru",
                currency="USD",
                seo_title="LocalMarket — Online Store",
                seo_description="Best products at best prices",
            )
        )


def _seed_themes(db):
    """Generate 300 themes across categories."""
    existing_count = db.query(Theme).count()
    if existing_count >= 300:
        return

    from app.core.themes_generator import generate_all_themes

    themes = generate_all_themes()
    for t in themes:
        exists = db.query(Theme).filter(Theme.slug == t["slug"]).first()
        if not exists:
            db.add(Theme(**t))


def _seed_demo_data(db):
    """Seed 20 categories and 400 products with images if empty."""
    if db.query(Product).count() >= 400:
        return

    from app.core.seed_products import CATEGORIES as SEED_CATEGORIES
    from app.core.seed_products import generate_all_products

    # Create categories
    cat_map: dict[str, int] = {}
    for cat_data in SEED_CATEGORIES:
        existing = db.query(Category).filter(Category.slug == cat_data["slug"]).first()
        if existing:
            cat_map[cat_data["slug"]] = existing.id
        else:
            cat = Category(**cat_data)
            db.add(cat)
            db.flush()
            cat_map[cat_data["slug"]] = cat.id

    # Create products
    all_products = generate_all_products()
    for p_data in all_products:
        existing = db.query(Product).filter(Product.slug == p_data["slug"]).first()
        if existing:
            continue
        cat_slug = p_data.pop("category_slug")
        p_data["category_id"] = cat_map.get(cat_slug)
        db.add(Product(**p_data))


# --- Public endpoints ---
@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/api/i18n/{lang}")
async def get_i18n(lang: str):
    """Return translations for a given language code."""
    return {
        "lang": lang,
        "translations": get_translations(lang),
    }


@app.get("/api/i18n")
async def list_languages():
    """Return all supported languages."""
    return {
        "languages": SUPPORTED_LANGUAGES,
        "names": LANGUAGE_NAMES,
    }
