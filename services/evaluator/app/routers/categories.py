"""Category CRUD endpoints — public read + admin write."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.product import Category
from app.models.user import User
from app.schemas.product import CategoryCreate, CategoryOut, CategoryUpdate

router = APIRouter()


@router.get("/categories", response_model=list[CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    """Public: list all categories."""
    return db.query(Category).order_by(Category.sort_order, Category.name).all()


@router.get("/categories/{slug}", response_model=CategoryOut)
def get_category(slug: str, db: Session = Depends(get_db)):
    """Public: get category by slug."""
    cat = db.query(Category).filter(Category.slug == slug).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    return cat


# --- Admin ---
@router.post("/admin/categories", response_model=CategoryOut, status_code=201)
def create_category(
    body: CategoryCreate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    cat = Category(**body.model_dump())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat


@router.patch("/admin/categories/{cat_id}", response_model=CategoryOut)
def update_category(
    cat_id: int,
    body: CategoryUpdate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    cat = db.query(Category).filter(Category.id == cat_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    for key, value in body.model_dump(exclude_unset=True).items():
        setattr(cat, key, value)
    db.commit()
    db.refresh(cat)
    return cat


@router.delete("/admin/categories/{cat_id}")
def delete_category(
    cat_id: int,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    cat = db.query(Category).filter(Category.id == cat_id).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(cat)
    db.commit()
    return {"message": "Category deleted"}
