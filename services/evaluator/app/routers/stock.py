"""Stock / inventory management endpoints (admin only)."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.product import Product, StockMovement
from app.models.user import User
from app.schemas.product import StockMovementCreate, StockMovementOut

router = APIRouter()


@router.get("/stock", response_model=list[StockMovementOut])
def list_stock_movements(
    product_id: int | None = None,
    skip: int = 0,
    limit: int = Query(default=50, le=500),
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    """Admin: list stock movements with optional product filter."""
    q = db.query(StockMovement)
    if product_id is not None:
        q = q.filter(StockMovement.product_id == product_id)
    return q.order_by(StockMovement.created_at.desc()).offset(skip).limit(limit).all()


@router.post("/stock", response_model=StockMovementOut, status_code=201)
def create_stock_movement(
    body: StockMovementCreate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    """Admin: record a stock movement (purchase, adjustment, return)."""
    product = db.query(Product).filter(Product.id == body.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.stock += body.quantity
    if product.stock < 0:
        raise HTTPException(status_code=400, detail="Stock cannot go below zero")

    movement = StockMovement(**body.model_dump())
    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement


@router.get("/stock/summary")
def stock_summary(
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    """Admin: overview of inventory — total products, total stock, low-stock items."""
    from sqlalchemy import func

    total_products = db.query(func.count(Product.id)).scalar() or 0
    total_stock = db.query(func.sum(Product.stock)).scalar() or 0
    low_stock = (
        db.query(Product)
        .filter(Product.stock < 10, Product.is_active.is_(True))
        .order_by(Product.stock)
        .limit(20)
        .all()
    )
    return {
        "total_products": total_products,
        "total_stock": int(total_stock),
        "low_stock_items": [
            {"id": p.id, "name": p.name, "sku": p.sku, "stock": p.stock}
            for p in low_stock
        ],
    }
