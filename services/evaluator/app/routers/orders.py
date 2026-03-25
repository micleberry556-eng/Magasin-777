"""Order endpoints — public create + admin manage."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_admin
from app.models.order import Order, OrderItem
from app.models.product import Product, StockMovement
from app.models.user import User
from app.schemas.order import OrderCreate, OrderOut, OrderStatusUpdate

router = APIRouter()


@router.post("/orders", response_model=OrderOut, status_code=201)
def create_order(body: OrderCreate, db: Session = Depends(get_db)):
    """Public: place a new order."""
    order = Order(
        customer_name=body.customer_name,
        customer_email=body.customer_email,
        customer_phone=body.customer_phone,
        customer_address=body.customer_address,
        note=body.note,
    )
    total = 0.0
    for item in body.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=400, detail=f"Product {item.product_id} not found")
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for {product.name}",
            )
        line_total = float(product.price) * item.quantity
        total += line_total
        order.items.append(
            OrderItem(
                product_id=product.id,
                product_name=product.name,
                quantity=item.quantity,
                price=float(product.price),
            )
        )
        # Decrease stock
        product.stock -= item.quantity
        product.sales_count += item.quantity
        db.add(
            StockMovement(
                product_id=product.id,
                quantity=-item.quantity,
                reason="sale",
                note=f"Order placed",
            )
        )
    order.total_amount = round(total, 2)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


# --- Admin ---
@router.get("/admin/orders", response_model=list[OrderOut])
def admin_list_orders(
    status: str | None = None,
    skip: int = 0,
    limit: int = Query(default=50, le=500),
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    """Admin: list orders with optional status filter."""
    q = db.query(Order)
    if status:
        q = q.filter(Order.status == status)
    return q.order_by(Order.created_at.desc()).offset(skip).limit(limit).all()


@router.get("/admin/orders/{order_id}", response_model=OrderOut)
def admin_get_order(
    order_id: int,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.patch("/admin/orders/{order_id}/status", response_model=OrderOut)
def update_order_status(
    order_id: int,
    body: OrderStatusUpdate,
    _admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = body.status
    db.commit()
    db.refresh(order)
    return order
