"""Data sanitization utilities."""
import re
from typing import Any, Dict


class DataSanitizer:
    """Sanitize user input data."""

    @staticmethod
    def sanitize_string(value: str) -> str:
        """Remove leading/trailing whitespace and normalize."""
        if not isinstance(value, str):
            return value
        return value.strip()

    @staticmethod
    def sanitize_email(email: str) -> str:
        """Sanitize email address."""
        if not isinstance(email, str):
            email = str(email)
        return DataSanitizer.sanitize_string(email).lower()

    @staticmethod
    def sanitize_username(username: str) -> str:
        """Sanitize username."""
        return DataSanitizer.sanitize_string(username).lower()

    @staticmethod
    def sanitize_phone(phone: str) -> str:
        """Remove non-numeric characters from phone."""
        if not isinstance(phone, str):
            return phone
        return re.sub(r'[^\d]', '', phone)

    @staticmethod
    def sanitize_user_data(data: Dict[str, Any]) -> Dict[str, Any]:
        """Sanitize all user registration data."""
        sanitized = data.copy()

        if 'firstname' in sanitized:
            sanitized['firstname'] = DataSanitizer.sanitize_string(str(sanitized['firstname']))
        if 'lastname' in sanitized:
            sanitized['lastname'] = DataSanitizer.sanitize_string(str(sanitized['lastname']))
        if 'email' in sanitized:
            sanitized['email'] = DataSanitizer.sanitize_email(str(sanitized['email']))
        if 'username' in sanitized:
            sanitized['username'] = DataSanitizer.sanitize_username(str(sanitized['username']))
        if 'mobilenumber' in sanitized:
            sanitized['mobilenumber'] = str(sanitized['mobilenumber'])
        if 'countrycode' in sanitized:
            sanitized['countrycode'] = DataSanitizer.sanitize_string(str(sanitized['countrycode']))

        # Add password sanitization
        if 'password' in sanitized:
            sanitized['password'] = str(sanitized['password']).strip()
        if 'confirmpassword' in sanitized:
            sanitized['confirmpassword'] = str(sanitized['confirmpassword']).strip()

        return sanitized
