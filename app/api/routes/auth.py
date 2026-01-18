from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, TokenResponse
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
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    token = authenticate_user(db, data.email, data.password)

    if not token:
        raise HTTPException(status_code=401, detail="Credenciais invalidas")

    return {"access_token": token}
