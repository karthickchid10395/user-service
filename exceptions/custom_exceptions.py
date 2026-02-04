"""Custom exceptions for the application."""


class BaseUserServiceException(Exception):
    """Base exception class for user service."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class UserAlreadyExistsException(BaseUserServiceException):
    """Exception raised when user already exists."""
    pass


class DuplicateUserException(BaseUserServiceException):
    """Exception raised when duplicate user is detected (username, email, or mobile)."""
    pass


class ValidationException(BaseUserServiceException):
    """Exception raised for validation errors."""
    pass


class UserNotFoundException(BaseUserServiceException):
    """Exception raised when user is not found."""
    pass


class AuthenticationException(BaseUserServiceException):
    """Exception raised for authentication failures."""
    pass


class DatabaseException(BaseUserServiceException):
    """Exception raised for database-related errors."""
    pass
