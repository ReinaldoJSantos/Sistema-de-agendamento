from pytest import Session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import (
    verify_password,
    create_access_token,
    get_password_hash
    )

from app.schemas.user import UserCreate


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, email: str, password: str):
        if self.repo.get_by_email(email):
            raise ValueError("Usuário já existe")

        hashed = get_password_hash(password)
        return self.repo.create(email, hashed, role="client")

    def login(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Credenciais inválidas")

        token = create_access_token({"sub": str(user.id), "role": user.role})
        return token

    def create_user(db: Session, user: UserCreate):
        db_user = User(
            email=user.email,
            hashed_password=get_password_hash(user.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
