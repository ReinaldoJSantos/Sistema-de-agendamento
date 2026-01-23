from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.auth import TokenResponse
from app.services.auth_service import authenticate_user
from app.api.dependencies import get_db
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    service = UserService(UserRepository(db))
    try:
        return service.register(email, password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    token = authenticate_user(db, form_data.username, form_data.password)

    if not token:
        raise HTTPException(status_code=401, detail="Credenciais invalidas")

    return {
        "access_token": token
        }
