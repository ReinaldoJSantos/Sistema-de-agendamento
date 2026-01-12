from sqlalchemy import Column, Integer, String
from app.core.database import Base


class HealtChech(Base):
    __tablename__ = "healt_check"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)

    