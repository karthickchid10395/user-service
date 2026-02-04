"""Constants for validation patterns and messages."""

class RegexPatterns:
    """Regex patterns for input validation."""
    ALPHA_ONLY = r'^[A-Za-z]+$'
    ALPHANUMERIC = r'^[A-Za-z0-9]+$'
    PASSWORD = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    COUNTRY_CODE = r'^\+\d{1,4}$'
    MOBILE_NUMBER = r'^\d{10,15}$'


class ValidationMessages:
    """Validation error messages."""
    FIRSTNAME_INVALID = "First name must contain only alphabetic characters"
    LASTNAME_INVALID = "Last name must contain only alphabetic characters"
    EMAIL_INVALID = "Invalid email format"
    PASSWORD_INVALID = "Password must be at least 8 characters with letters, numbers, and special characters (@$!%*#?&)"
    PASSWORD_MISMATCH = "Password and confirm password do not match"
    COUNTRY_CODE_INVALID = "Country code must start with + followed by 1-4 digits"
    MOBILE_INVALID = "Mobile number must be 10-15 digits"
    USERNAME_INVALID = "Username must be alphanumeric"
    USERNAME_EXISTS = "Username already exists"
    EMAIL_EXISTS = "Email already registered"
    MOBILE_EXISTS = "Mobile number already registered"


class ResponseMessages:
    """API response messages."""
    USER_CREATED = "User created successfully"
    INTERNAL_ERROR = "Internal server error occurred"
    VALIDATION_ERROR = "Validation error"
