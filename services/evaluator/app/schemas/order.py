"""Order schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = 1


class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str = ""
    customer_phone: str = ""
    customer_address: str = ""
    note: str = ""
    items: list[OrderItemCreate]


class OrderStatusUpdate(BaseModel):
    status: str  # new, processing, shipped, delivered, cancelled


class OrderItemOut(BaseModel):
    id: int
    product_id: int
    product_name: str
    quantity: int
    price: float

    model_config = {"from_attributes": True}


class OrderOut(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    customer_phone: str
    customer_address: str
    status: str
    total_amount: float
    note: str
    items: list[OrderItemOut]
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
