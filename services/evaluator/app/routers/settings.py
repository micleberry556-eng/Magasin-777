"""Site settings endpoints — public read + admin write."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.site import SiteSettings
from app.models.user import User
from app.schemas.site import SiteSettingsOut, SiteSettingsUpdate

router = APIRouter()


@router.get("/settings", response_model=SiteSettingsOut)
def get_settings(db: Session = Depends(get_db)):
    """Public: get current site settings."""
    settings = db.query(SiteSettings).first()
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not initialized")
    return settings


@router.patch("/admin/settings", response_model=SiteSettingsOut)
def update_settings(
    body: SiteSettingsUpdate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    """Admin: update site settings (name, SEO, language, theme, etc.)."""
    settings = db.query(SiteSettings).first()
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not initialized")
    for key, value in body.model_dump(exclude_unset=True).items():
        setattr(settings, key, value)
    db.commit()
    db.refresh(settings)
    return settings
