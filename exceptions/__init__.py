"""Custom exceptions module."""
from .custom_exceptions import (
    BaseUserServiceException,
    UserAlreadyExistsException,
    DuplicateUserException,
    ValidationException,
    UserNotFoundException,
    AuthenticationException,
    DatabaseException
)

__all__ = [
    'BaseUserServiceException',
    'UserAlreadyExistsException',
    'DuplicateUserException',
    'ValidationException',
    'UserNotFoundException',
    'AuthenticationException',
    'DatabaseException'
]

