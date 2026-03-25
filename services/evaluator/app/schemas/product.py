"""Product and category schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# --- Category ---
class CategoryCreate(BaseModel):
    name: str
    slug: str
    parent_id: Optional[int] = None
    image: str = ""
    sort_order: int = 0


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    parent_id: Optional[int] = None
    image: Optional[str] = None
    sort_order: Optional[int] = None


class CategoryOut(BaseModel):
    id: int
    name: str
    slug: str
    parent_id: Optional[int]
    image: str
    sort_order: int

    model_config = {"from_attributes": True}


# --- Product ---
class ProductCreate(BaseModel):
    name: str
    slug: str
    description: str = ""
    price: float
    old_price: Optional[float] = None
    sku: str = ""
    stock: int = 0
    category_id: Optional[int] = None
    image: str = ""
    images: str = "[]"
    is_active: bool = True
    is_featured: bool = False
    seo_title: str = ""
    seo_description: str = ""


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    old_price: Optional[float] = None
    sku: Optional[str] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None
    image: Optional[str] = None
    images: Optional[str] = None
    is_active: Optional[bool] = None
    is_featured: Optional[bool] = None
    seo_title: Optional[str] = None
    seo_description: Optional[str] = None


class ProductOut(BaseModel):
    id: int
    name: str
    slug: str
    description: str
    price: float
    old_price: Optional[float]
    sku: str
    stock: int
    category_id: Optional[int]
    image: str
    images: str
    rating: float
    sales_count: int
    is_active: bool
    is_featured: bool
    seo_title: str
    seo_description: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# --- Stock Movement ---
class StockMovementCreate(BaseModel):
    product_id: int
    quantity: int
    reason: str  # purchase, sale, adjustment, return
    note: str = ""


class StockMovementOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    reason: str
    note: str
    created_at: datetime

    model_config = {"from_attributes": True}
