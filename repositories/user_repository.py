"""Repository layer for user data access."""
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.user import User
from typing import Optional


class UserRepository:
    """Repository for user database operations."""

    def __init__(self, db: Session):
        self.db = db

    def find_by_username(self, username: str) -> Optional[User]:
        """Find user by username."""
        return self.db.query(User).filter(User.username == username).first()

    def find_by_email(self, email: str) -> Optional[User]:
        """Find user by email."""
        return self.db.query(User).filter(User.email == email).first()

    def find_by_full_mobile(self, full_mobile: str) -> Optional[User]:
        """Find user by full mobile number (country code + mobile)."""
        return self.db.query(User).filter(User.full_mobile == full_mobile).first()

    def create_user(self, user: User) -> User:
        """Create a new user."""
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            self.db.rollback()
            raise e
