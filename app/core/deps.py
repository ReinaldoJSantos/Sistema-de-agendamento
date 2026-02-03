from fastapi import Depends, HTTPException, status
from app.core.security import decode_access_token
from app.models.user import User
from sqlalchemy.orm import Session
from app.core.database import get_db


def get_current_user(
    payload: dict = Depends(decode_access_token),
    db: Session = Depends(get_db)
) -> User:
    # user = db.query(User).filter(User.id == token.sub).first()
    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
        )
    return user_id


def require_admin(
    currente_user: User = Depends(get_current_user),
) -> User:
    if not currente_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso restrito a administradores",
        )

    return currente_user

