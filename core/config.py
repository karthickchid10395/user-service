"""Application configuration."""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application Settings
    APP_NAME: str = "User Management Service"
    DEBUG: bool = True

    # Database Configuration
    DATABASE_URL: str = "postgresql://postgres:Python123@localhost:5432/user_mgmt"

    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Security Settings (for future use with JWT)
    SECRET_KEY: Optional[str] = None
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True


settings = Settings()
