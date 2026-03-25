"""Application configuration."""

import os

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:secret@postgres:5432/localmarket",
)

SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production-very-secret-key-2026")
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "/app/static/uploads")

# Default admin credentials (created on first run)
DEFAULT_ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL", "admin@localmarket.com")
DEFAULT_ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "admin123")
