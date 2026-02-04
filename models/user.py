"""User database model."""
from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.sql import func
from core.database import Base


class User(Base):
    """User model for database."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    country_code = Column(String(5), nullable=False)
    mobile_number = Column(String(15), nullable=False)
    full_mobile = Column(String(20), unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        Index('idx_email', 'email'),
        Index('idx_username', 'username'),
        Index('idx_full_mobile', 'full_mobile'),
    )
