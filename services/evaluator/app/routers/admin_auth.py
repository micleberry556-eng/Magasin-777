"""Admin authentication endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import (
    create_access_token,
    get_current_admin,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.schemas.auth import ChangePasswordRequest, LoginRequest, TokenResponse

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def admin_login(body: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate admin and return JWT token."""
    user = db.query(User).filter(User.email == body.email, User.role == "admin").first()
    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": str(user.id)})
    return TokenResponse(access_token=token)


@router.post("/change-password")
def change_password(
    body: ChangePasswordRequest,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db),
):
    """Change admin password."""
    if not verify_password(body.current_password, admin.password_hash):
        raise HTTPException(status_code=400, detail="Current password is incorrect")
    admin.password_hash = hash_password(body.new_password)
    db.commit()
    return {"message": "Password changed successfully"}


@router.get("/me")
def admin_me(admin: User = Depends(get_current_admin)):
    """Return current admin info."""
    return {"id": admin.id, "email": admin.email, "name": admin.name, "role": admin.role}
