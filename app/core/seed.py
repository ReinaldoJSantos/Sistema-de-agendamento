from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import get_password_hash
from app.core.config import settings


def create_admin_user(db: Session):
    admin = db.query(User).filter(
        User.email == settings.ADMIN_EMAIL
    ).first()

    if admin:
        return

    admin = User(
        email=settings.ADMIN_EMAIL,
        hashed_password=get_password_hash(settings.ADMIN_PASSWORD),
        role="admin"
    )

    db.add(admin)
    db.commit()