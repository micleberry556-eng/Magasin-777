"""File upload endpoint (admin only)."""

import os
import uuid

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from PIL import Image

from app.core.config import UPLOAD_DIR
from app.core.security import get_current_admin
from app.models.user import User

router = APIRouter()

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".ico"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post("/upload")
async def upload_file(
    file: UploadFile,
    _admin: User = Depends(get_current_admin),
):
    """Admin: upload an image file (logo, background, product image, etc.)."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")

    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type '{ext}' not allowed. Allowed: {', '.join(ALLOWED_EXTENSIONS)}",
        )

    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large (max 10 MB)")

    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)

    with open(filepath, "wb") as f:
        f.write(content)

    # Generate thumbnail for raster images
    thumb_url = ""
    if ext in {".jpg", ".jpeg", ".png", ".webp"}:
        try:
            img = Image.open(filepath)
            img.thumbnail((300, 300))
            thumb_name = f"thumb_{filename}"
            thumb_path = os.path.join(UPLOAD_DIR, thumb_name)
            img.save(thumb_path)
            thumb_url = f"/static/uploads/{thumb_name}"
        except Exception:
            pass  # Non-critical: skip thumbnail on error

    return {
        "url": f"/static/uploads/{filename}",
        "thumbnail": thumb_url,
        "filename": filename,
        "size": len(content),
    }
