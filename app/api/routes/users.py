from fastapi import APIRouter, Depends
from pytest import Session
from app.api.dependencies import get_current_user, get_db
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
