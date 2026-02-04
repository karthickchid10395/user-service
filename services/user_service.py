"""Business logic layer for user operations."""
import bcrypt
from typing import Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.user import User
from schemas.user_schema import UserRegisterRequest
from repositories.user_repository import UserRepository
from exceptions.custom_exceptions import (
    UserAlreadyExistsException,
    ValidationException,
    DuplicateUserException
)
from utils.constants import ValidationMessages, ResponseMessages
from utils.data_sanitizer import DataSanitizer
from utils.validators import PasswordStrengthChecker


class UserService:
    """Service layer for user business logic."""

    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)

    def _hash_password(self, password: str) -> str:
        """Hash password using bcrypt."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def _check_user_exists(self, request: UserRegisterRequest) -> None:
        """Check if user already exists with username, email, or mobile."""
        if self.repository.find_by_username(str(request.username)):
            raise UserAlreadyExistsException(ValidationMessages.USERNAME_EXISTS)

        if self.repository.find_by_email(str(request.email)):
            raise UserAlreadyExistsException(ValidationMessages.EMAIL_EXISTS)

        full_mobile = f"{request.countrycode}{request.mobilenumber}"
        if self.repository.find_by_full_mobile(full_mobile):
            raise UserAlreadyExistsException(ValidationMessages.MOBILE_EXISTS)

    def register_user(self, request: UserRegisterRequest) -> Dict[str, Any]:
        """Register a new user.

        Args:
            request: User registration request with validated data

        Returns:
            Dictionary containing user id, username, email, and success message

        Raises:
            ValidationException: If validation fails
            UserAlreadyExistsException: If user already exists
            DuplicateUserException: If duplicate data found in database
        """
        # Convert Pydantic model to dict
        data = request.model_dump()

        # Sanitize data
        sanitized_data = DataSanitizer.sanitize_user_data(data)

        # Validate password match
        if sanitized_data['password'] != sanitized_data['confirmpassword']:
            raise ValidationException("Passwords do not match")

        # Check password strength
        strength = PasswordStrengthChecker.check_password_strength(
            sanitized_data['password']
        )
        if not strength['is_strong']:
            raise ValidationException(
                f"Weak password: {', '.join(strength['feedback'])}"
            )

        # Create sanitized request object for duplicate checks
        sanitized_request = UserRegisterRequest(**sanitized_data)

        # Check if user already exists (uses sanitized values)
        self._check_user_exists(sanitized_request)

        # Create user model
        full_mobile = f"{sanitized_request.countrycode}{sanitized_request.mobilenumber}"
        password_hash = self._hash_password(sanitized_request.password)

        user = User(
            firstname=sanitized_data['firstname'],
            lastname=sanitized_data['lastname'],
            email=sanitized_data['email'],
            username=sanitized_data['username'],
            password_hash=password_hash,
            country_code=sanitized_request.countrycode,
            mobile_number=sanitized_request.mobilenumber,
            full_mobile=full_mobile
        )

        try:
            # Save to database
            created_user = self.repository.create_user(user)

            return {
                'id': created_user.id,
                'username': created_user.username,
                'email': created_user.email,
                'message': ResponseMessages.USER_CREATED
            }
        except IntegrityError as e:
            self.db.rollback()
            raise DuplicateUserException(
                "User with this username, email, or mobile already exists"
            )
        except Exception as e:
            self.db.rollback()
            raise ValidationException(f"Registration failed: {str(e)}")
