"""API routes for user operations."""
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.orm import Session

from core.database import get_db
from exceptions.custom_exceptions import (
    UserAlreadyExistsException
)
from schemas.user_schema import UserRegisterRequest, UserRegisterResponse
from services.user_service import UserService
from utils.constants import ResponseMessages
from utils.data_sanitizer import DataSanitizer  # Add this line

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post(
    "/register",
    response_model=UserRegisterResponse,
    status_code=status.HTTP_201_CREATED
)
async def register_user(
        request: UserRegisterRequest,
        db: Session = Depends(get_db)
):
    """
    Register a new user.

    - **firstname**: Alphabetic characters only
    - **lastname**: Alphabetic characters only
    - **email**: Valid email format
    - **password**: Min 8 chars with letters, numbers, and special chars
    - **confirmpassword**: Must match password
    - **countrycode**: Format: +{1-4 digits}
    - **mobilenumber**: 10-15 digits
    - **username**: Alphanumeric only
    """
    try:

        sanitized_data = DataSanitizer.sanitize_user_data(request.model_dump())

        # Update original request object instead of creating new one
        for key, value in sanitized_data.items():
            setattr(request, key, value)

        service = UserService(db)
        service.register_user(request)

        return UserRegisterResponse(message=ResponseMessages.USER_CREATED)

    except UserAlreadyExistsException as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": ResponseMessages.VALIDATION_ERROR,
                "errorInfo": {"detail": str(e.message)}
            }
        )

    except ValidationError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": ResponseMessages.VALIDATION_ERROR,
                "errorInfo": {"detail": e.errors()}
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": ResponseMessages.INTERNAL_ERROR,
                "errorInfo": {"detail": str(e)}
            }
        )
