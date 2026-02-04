"""Pydantic schemas for user validation."""
from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import Optional
from utils.validators import InputValidator


class UserRegisterRequest(BaseModel):
    """Schema for user registration request with comprehensive validation."""

    firstname: str
    lastname: str
    email: EmailStr
    username: str
    password: str
    confirmpassword: str
    countrycode: str
    mobilenumber: str

    @field_validator('firstname')
    @classmethod
    def validate_firstname(cls, v: str) -> str:
        """Validate first name using InputValidator."""
        is_valid, error = InputValidator.validate_alpha(v, 'First name')
        if not is_valid:
            raise ValueError(error)
        return InputValidator.sanitize_input(v).capitalize()

    @field_validator('lastname')
    @classmethod
    def validate_lastname(cls, v: str) -> str:
        """Validate last name using InputValidator."""
        is_valid, error = InputValidator.validate_alpha(v, 'Last name')
        if not is_valid:
            raise ValueError(error)
        return InputValidator.sanitize_input(v).capitalize()

    @field_validator('username')
    @classmethod
    def validate_username(cls, v: str) -> str:
        """Validate username using InputValidator."""
        is_valid, error = InputValidator.validate_alphanumeric(v, 'Username')
        if not is_valid:
            raise ValueError(error)
        return InputValidator.sanitize_input(v).lower()

    @field_validator('email')
    @classmethod
    def validate_email_format(cls, v: str) -> str:
        """Additional email validation using InputValidator."""
        is_valid, error = InputValidator.validate_email(v)
        if not is_valid:
            raise ValueError(error)
        return InputValidator.sanitize_email(v)

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Validate password using InputValidator."""
        is_valid, error = InputValidator.validate_password(v)
        if not is_valid:
            raise ValueError(error)
        return v

    @field_validator('countrycode')
    @classmethod
    def validate_countrycode(cls, v: str) -> str:
        """Validate country code using InputValidator."""
        is_valid, error = InputValidator.validate_country_code(v)
        if not is_valid:
            raise ValueError(error)
        return InputValidator.sanitize_input(v)

    @field_validator('mobilenumber')
    @classmethod
    def validate_mobilenumber(cls, v: str) -> str:
        """Validate mobile number using InputValidator."""
        is_valid, error = InputValidator.validate_mobile_number(v)
        if not is_valid:
            raise ValueError(error)
        return InputValidator.sanitize_input(v)

    @model_validator(mode='after')
    def validate_passwords_match(self):
        """Validate that password and confirm password match."""
        is_valid, error = InputValidator.validate_passwords_match(
            self.password,
            self.confirmpassword
        )
        if not is_valid:
            raise ValueError(error)
        return self

    class Config:
        """Pydantic config."""
        str_strip_whitespace = True
        json_schema_extra = {
            "example": {
                "firstname": "John",
                "lastname": "Doe",
                "email": "john.doe@example.com",
                "username": "johndoe123",
                "password": "SecurePass123!",
                "confirmpassword": "SecurePass123!",
                "countrycode": "+1",
                "mobilenumber": "1234567890"
            }
        }


class UserRegisterResponse(BaseModel):
    """Schema for user registration response."""

    message: str
    errorInfo: Optional[dict] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "message": "User registered successfully",
                "errorInfo": None
            }
        }


class UserResponse(BaseModel):
    """Schema for user data response."""

    id: int
    firstname: str
    lastname: str
    email: str
    username: str
    countrycode: str
    mobilenumber: str

    class Config:
        from_attributes = True
