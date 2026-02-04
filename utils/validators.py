"""Utility functions and classes for comprehensive input validation."""
import re
from typing import Tuple, Optional, Dict, Any
from utils.constants import RegexPatterns, ValidationMessages


class InputValidator:
    """Class for validating user inputs with comprehensive validation logic."""

    @staticmethod
    def validate_alpha(value: str, field_name: str) -> Tuple[bool, Optional[str]]:
        """
        Validate alphabetic input (firstname, lastname).

        Args:
            value: Input string to validate
            field_name: Name of the field for error message

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not value:
            return False, f"{field_name} is required"

        value = value.strip()

        if not re.match(RegexPatterns.ALPHA_ONLY, value):
            return False, f"{field_name} must contain only alphabetic characters"

        if len(value) < 2:
            return False, f"{field_name} must be at least 2 characters long"

        if len(value) > 50:
            return False, f"{field_name} must not exceed 50 characters"

        return True, None

    @staticmethod
    def validate_alphanumeric(value: str, field_name: str) -> Tuple[bool, Optional[str]]:
        """
        Validate alphanumeric input (username).

        Args:
            value: Input string to validate
            field_name: Name of the field for error message

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not value:
            return False, f"{field_name} is required"

        value = value.strip()

        if not re.match(RegexPatterns.ALPHANUMERIC, value):
            return False, ValidationMessages.USERNAME_INVALID

        if len(value) < 3:
            return False, f"{field_name} must be at least 3 characters long"

        if len(value) > 30:
            return False, f"{field_name} must not exceed 30 characters"

        return True, None

    @staticmethod
    def validate_email(email: str) -> Tuple[bool, Optional[str]]:
        """
        Validate email format.

        Args:
            email: Email address to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not email:
            return False, "Email is required"

        email = email.strip().lower()

        # Basic email regex pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(email_pattern, email):
            return False, ValidationMessages.EMAIL_INVALID

        if len(email) > 255:
            return False, "Email must not exceed 255 characters"

        return True, None

    @staticmethod
    def validate_password(password: str) -> Tuple[bool, Optional[str]]:
        """
        Validate password strength.
        Must contain: letters, numbers, special characters (@$!%*#?&)
        Minimum 8 characters.

        Args:
            password: Password to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not password:
            return False, "Password is required"

        if len(password) < 8:
            return False, "Password must be at least 8 characters long"

        if len(password) > 128:
            return False, "Password must not exceed 128 characters"

        if not re.match(RegexPatterns.PASSWORD, password):
            return False, ValidationMessages.PASSWORD_INVALID

        return True, None

    @staticmethod
    def validate_passwords_match(password: str, confirm_password: str) -> Tuple[bool, Optional[str]]:
        """
        Validate that password and confirm password match.

        Args:
            password: Original password
            confirm_password: Confirmation password

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not confirm_password:
            return False, "Confirm password is required"

        if password != confirm_password:
            return False, ValidationMessages.PASSWORD_MISMATCH

        return True, None

    @staticmethod
    def validate_country_code(country_code: str) -> Tuple[bool, Optional[str]]:
        """
        Validate country code format (+1 to +9999).

        Args:
            country_code: Country code to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not country_code:
            return False, "Country code is required"

        country_code = country_code.strip()

        if not re.match(RegexPatterns.COUNTRY_CODE, country_code):
            return False, ValidationMessages.COUNTRY_CODE_INVALID

        # Extract numeric part and validate range
        numeric_part = country_code[1:]
        try:
            code_number = int(numeric_part)
            if code_number < 1 or code_number > 9999:
                return False, "Country code must be between +1 and +9999"
        except ValueError:
            return False, ValidationMessages.COUNTRY_CODE_INVALID

        return True, None

    @staticmethod
    def validate_mobile_number(mobile: str) -> Tuple[bool, Optional[str]]:
        """
        Validate mobile number format (10-15 digits).

        Args:
            mobile: Mobile number to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not mobile:
            return False, "Mobile number is required"

        mobile = mobile.strip()

        if not re.match(RegexPatterns.MOBILE_NUMBER, mobile):
            return False, ValidationMessages.MOBILE_INVALID

        return True, None

    @staticmethod
    def sanitize_input(value: str) -> str:
        """
        Sanitize input by stripping whitespace and normalizing.

        Args:
            value: Input string to sanitize

        Returns:
            Sanitized string
        """
        if not value:
            return ""

        # Strip whitespace
        sanitized = value.strip()

        # Remove multiple consecutive spaces
        sanitized = re.sub(r'\s+', ' ', sanitized)

        return sanitized

    @staticmethod
    def sanitize_email(email: str) -> str:
        """
        Sanitize email by converting to lowercase and stripping whitespace.

        Args:
            email: Email address to sanitize

        Returns:
            Sanitized email
        """
        if not email:
            return ""

        return email.strip().lower()

    @staticmethod
    def validate_all_registration_inputs(data: Dict[str, Any]) -> Dict[str, str]:
        """
        Validate all registration inputs and return all errors.

        Args:
            data: Dictionary containing all registration fields

        Returns:
            Dictionary of field_name: error_message for all invalid fields
        """
        errors = {}

        # Validate firstname
        is_valid, error = InputValidator.validate_alpha(
            data.get('firstname', ''), 'First name'
        )
        if not is_valid:
            errors['firstname'] = error

        # Validate lastname
        is_valid, error = InputValidator.validate_alpha(
            data.get('lastname', ''), 'Last name'
        )
        if not is_valid:
            errors['lastname'] = error

        # Validate email
        is_valid, error = InputValidator.validate_email(
            data.get('email', '')
        )
        if not is_valid:
            errors['email'] = error

        # Validate username
        is_valid, error = InputValidator.validate_alphanumeric(
            data.get('username', ''), 'Username'
        )
        if not is_valid:
            errors['username'] = error

        # Validate password
        password = data.get('password', '')
        is_valid, error = InputValidator.validate_password(password)
        if not is_valid:
            errors['password'] = error

        # Validate confirm password
        confirm_password = data.get('confirmpassword', '')
        is_valid, error = InputValidator.validate_passwords_match(
            password, confirm_password
        )
        if not is_valid:
            errors['confirmpassword'] = error

        # Validate country code
        is_valid, error = InputValidator.validate_country_code(
            data.get('countrycode', '')
        )
        if not is_valid:
            errors['countrycode'] = error

        # Validate mobile number
        is_valid, error = InputValidator.validate_mobile_number(
            data.get('mobilenumber', '')
        )
        if not is_valid:
            errors['mobilenumber'] = error

        return errors


class PasswordStrengthChecker:
    """Advanced password strength validation."""

    @staticmethod
    def check_password_strength(password: str) -> Dict[str, Any]:
        """
        Check password strength and provide detailed feedback.

        Args:
            password: Password to check

        Returns:
            Dictionary with strength score and feedback
        """
        strength = {
            'score': 0,
            'is_strong': False,
            'feedback': []
        }

        if not password:
            strength['feedback'].append("Password is required")
            return strength

        # Length check
        if len(password) >= 8:
            strength['score'] += 1
        else:
            strength['feedback'].append("Password should be at least 8 characters")

        if len(password) >= 12:
            strength['score'] += 1

        # Character type checks
        if re.search(r'[a-z]', password):
            strength['score'] += 1
        else:
            strength['feedback'].append("Add lowercase letters")

        if re.search(r'[A-Z]', password):
            strength['score'] += 1
        else:
            strength['feedback'].append("Add uppercase letters")

        if re.search(r'\d', password):
            strength['score'] += 1
        else:
            strength['feedback'].append("Add numbers")

        if re.search(r'[@$!%*#?&]', password):
            strength['score'] += 1
        else:
            strength['feedback'].append("Add special characters (@$!%*#?&)")

        # Determine if strong
        strength['is_strong'] = strength['score'] >= 5

        if not strength['feedback']:
            strength['feedback'].append("Strong password")

        return strength

