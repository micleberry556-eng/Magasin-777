"""
LocalMarket Evaluator Service
==============================
Web-сервис оценки товаров и расчёта комиссий.
Поддерживает встроенный алгоритм и проксирование к внешнему сервису.
"""

import os
from typing import Dict, Optional

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="LocalMarket Evaluator Service",
    description="Сервис оценки товаров и расчёта комиссий маркетплейса",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class EvaluateRequest(BaseModel):
    """Запрос на оценку товара."""

    product_id: Optional[str] = None
    seller_id: Optional[str] = None
    base_price: float
    params: Optional[Dict[str, float | int | str]] = {}


class EvaluateResponse(BaseModel):
    """Результат оценки товара."""

    score: float
    recommended_price: float
    commission_percent: float
    rationale: str


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

EXTERNAL_URL: str = os.getenv("EVALUATOR_EXTERNAL_URL", "")

# ---------------------------------------------------------------------------
# Evaluation Logic
# ---------------------------------------------------------------------------

# Базовые комиссии по категориям (%)
CATEGORY_COMMISSIONS: Dict[str, float] = {
    "electronics": 10.0,
    "clothing": 12.0,
    "food": 8.0,
    "default": 15.0,
}

# Максимальные референсные значения для нормализации
MAX_RATING = 5.0
MAX_SALES_VELOCITY = 100  # продаж в месяц

# Весовые коэффициенты для расчёта score
WEIGHT_RATING = 0.6
WEIGHT_SALES = 0.4

# Порог рейтинга для скидки за лояльность
LOYALTY_RATING_THRESHOLD = 4.5
LOYALTY_DISCOUNT = 0.05  # 5% скидка к комиссии


def local_evaluation(data: EvaluateRequest) -> EvaluateResponse:
    """
    Встроенный алгоритм оценки (раздел 13 ТЗ).

    1. Score (0..100) = normalize(rating * 0.6 + sales_velocity * 0.4)
    2. Комиссия зависит от категории и лояльности продавца.
    3. Рекомендуемая цена = base_price * margin_factor(score).
    """
    params = data.params or {}
    rating = float(params.get("rating", 4.0))
    sales_velocity = int(params.get("sales_velocity", 10))
    category = str(params.get("category", "default"))

    # 1. Расчёт Score (0..100)
    norm_rating = (rating / MAX_RATING) * 100
    norm_sales = min((sales_velocity / MAX_SALES_VELOCITY) * 100, 100)
    score = (norm_rating * WEIGHT_RATING) + (norm_sales * WEIGHT_SALES)

    # 2. Расчёт комиссии
    base_commission = CATEGORY_COMMISSIONS.get(
        category, CATEGORY_COMMISSIONS["default"]
    )
    loyalty_discount = LOYALTY_DISCOUNT if rating > LOYALTY_RATING_THRESHOLD else 0.0
    commission_percent = base_commission * (1 - loyalty_discount)

    # 3. Рекомендуемая цена
    margin_factor = 1.0 + (score / 1000.0)
    recommended_price = data.base_price * margin_factor

    return EvaluateResponse(
        score=round(score, 2),
        recommended_price=round(recommended_price, 2),
        commission_percent=round(commission_percent, 2),
        rationale=(
            f"Score calculated: rating={rating} (weight {WEIGHT_RATING}), "
            f"sales_velocity={sales_velocity} (weight {WEIGHT_SALES}). "
            f"Category '{category}' base commission {base_commission}%."
            + (" Loyalty discount applied." if loyalty_discount > 0 else "")
        ),
    )


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------


@app.post("/api/v1/evaluate", response_model=EvaluateResponse)
async def evaluate_product(request: EvaluateRequest) -> EvaluateResponse:
    """
    Точка входа для оценки товара.

    Если задан EVALUATOR_EXTERNAL_URL — проксирует запрос к внешнему сервису.
    При ошибке или отсутствии URL — использует встроенный алгоритм.
    """
    if EXTERNAL_URL:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    EXTERNAL_URL,
                    json=request.model_dump(),
                    timeout=5.0,
                )
                if response.status_code == 200:
                    return EvaluateResponse(**response.json())
        except Exception as exc:
            # Fallback на локальный расчёт при ошибке внешнего сервиса
            print(f"External evaluator failed: {exc}. Falling back to local.")

    return local_evaluation(request)


@app.get("/health")
async def health() -> dict[str, str]:
    """Проверка работоспособности сервиса."""
    return {"status": "ok"}
