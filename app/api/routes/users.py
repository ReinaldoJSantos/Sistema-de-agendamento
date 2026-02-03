from fastapi import APIRouter, Depends
from pytest import Session
from app.core.deps import get_current_user, get_db, require_admin
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.user_service import UserService


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
    }


@router.post("/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)


@router.get("/admin-only")
def admin_area(admin_user: User = Depends(require_admin)):
    return {"message": f"Bem-vindo admin {admin_user.email}"}