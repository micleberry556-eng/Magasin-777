"""Theme endpoints — public read + admin activate."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.site import SiteSettings, Theme
from app.models.user import User
from app.schemas.site import ThemeOut

router = APIRouter()


@router.get("/themes", response_model=list[ThemeOut])
def list_themes(
    category: str | None = None,
    skip: int = 0,
    limit: int = Query(default=50, le=300),
    db: Session = Depends(get_db),
):
    """Public: list available themes with optional category filter."""
    q = db.query(Theme)
    if category:
        q = q.filter(Theme.category == category)
    return q.order_by(Theme.id).offset(skip).limit(limit).all()


@router.get("/themes/categories")
def list_theme_categories(db: Session = Depends(get_db)):
    """Public: list unique theme categories with counts."""
    from sqlalchemy import func

    rows = (
        db.query(Theme.category, func.count(Theme.id))
        .group_by(Theme.category)
        .order_by(Theme.category)
        .all()
    )
    return [{"category": cat, "count": cnt} for cat, cnt in rows]


@router.get("/themes/{theme_id}", response_model=ThemeOut)
def get_theme(theme_id: int, db: Session = Depends(get_db)):
    """Public: get theme by ID."""
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    return theme


@router.post("/admin/themes/{theme_id}/activate")
def activate_theme(
    theme_id: int,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    """Admin: set active theme for the site."""
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")
    settings = db.query(SiteSettings).first()
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not initialized")
    settings.active_theme_id = theme_id
    db.commit()
    return {"message": f"Theme '{theme.name}' activated", "theme_id": theme_id}
