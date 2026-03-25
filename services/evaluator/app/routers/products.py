"""Product CRUD endpoints — public read + admin write."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.product import Product
from app.models.user import User
from app.schemas.product import ProductCreate, ProductOut, ProductUpdate

router = APIRouter()


@router.get("/products", response_model=list[ProductOut])
def list_products(
    category_id: int | None = None,
    featured: bool | None = None,
    search: str | None = None,
    skip: int = 0,
    limit: int = Query(default=50, le=200),
    db: Session = Depends(get_db),
):
    """Public: list products with optional filters."""
    q = db.query(Product).filter(Product.is_active.is_(True))
    if category_id is not None:
        q = q.filter(Product.category_id == category_id)
    if featured is not None:
        q = q.filter(Product.is_featured.is_(featured))
    if search:
        q = q.filter(Product.name.ilike(f"%{search}%"))
    return q.order_by(Product.created_at.desc()).offset(skip).limit(limit).all()


@router.get("/products/{slug}", response_model=ProductOut)
def get_product(slug: str, db: Session = Depends(get_db)):
    """Public: get product by slug."""
    product = db.query(Product).filter(Product.slug == slug, Product.is_active.is_(True)).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# --- Admin ---
@router.get("/admin/products", response_model=list[ProductOut])
def admin_list_products(
    skip: int = 0,
    limit: int = Query(default=50, le=500),
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    """Admin: list all products including inactive."""
    return db.query(Product).order_by(Product.id.desc()).offset(skip).limit(limit).all()


@router.post("/admin/products", response_model=ProductOut, status_code=201)
def create_product(
    body: ProductCreate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    product = Product(**body.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.patch("/admin/products/{product_id}", response_model=ProductOut)
def update_product(
    product_id: int,
    body: ProductUpdate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in body.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


@router.delete("/admin/products/{product_id}")
def delete_product(
    product_id: int,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted"}
