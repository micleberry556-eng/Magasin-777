"""CMS page endpoints — public read + admin write."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.site import Page
from app.models.user import User
from app.schemas.site import PageCreate, PageOut, PageUpdate

router = APIRouter()


@router.get("/pages", response_model=list[PageOut])
def list_pages(db: Session = Depends(get_db)):
    """Public: list published pages."""
    return (
        db.query(Page)
        .filter(Page.is_published.is_(True))
        .order_by(Page.sort_order, Page.title)
        .all()
    )


@router.get("/pages/{slug}", response_model=PageOut)
def get_page(slug: str, db: Session = Depends(get_db)):
    """Public: get page by slug."""
    page = db.query(Page).filter(Page.slug == slug, Page.is_published.is_(True)).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    return page


# --- Admin ---
@router.get("/admin/pages", response_model=list[PageOut])
def admin_list_pages(
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    return db.query(Page).order_by(Page.sort_order, Page.title).all()


@router.post("/admin/pages", response_model=PageOut, status_code=201)
def create_page(
    body: PageCreate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    page = Page(**body.model_dump())
    db.add(page)
    db.commit()
    db.refresh(page)
    return page


@router.patch("/admin/pages/{page_id}", response_model=PageOut)
def update_page(
    page_id: int,
    body: PageUpdate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    page = db.query(Page).filter(Page.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    for key, value in body.model_dump(exclude_unset=True).items():
        setattr(page, key, value)
    db.commit()
    db.refresh(page)
    return page


@router.delete("/admin/pages/{page_id}")
def delete_page(
    page_id: int,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    page = db.query(Page).filter(Page.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    db.delete(page)
    db.commit()
    return {"message": "Page deleted"}
