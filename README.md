# User Management Microservice

A RESTful API microservice for user management built with FastAPI, following clean architecture principles.

## Features

- User registration with comprehensive validation
- Password strength validation
- Unique constraints on username, email, and mobile number
- Input sanitization and security best practices
- PostgreSQL database with SQLAlchemy ORM
- Swagger UI documentation
- Modular architecture (routes, services, repositories, models)

## Project Structure

```
user-service/
├── api/
│   └── routes/           # API endpoints
├── core/
│   ├── config.py        # Configuration settings
│   └── database.py      # Database connection
├── exceptions/          # Custom exceptions
├── models/              # SQLAlchemy models
├── repositories/        # Data access layer
├── schemas/             # Pydantic schemas
├── services/            # Business logic layer
├── utils/               # Utilities (validators, constants)
├── main.py              # Application entry point
└── requirements.txt     # Python dependencies
```

## Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher (or use SQLite for testing)
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository

```bash
cd C:\Users\SUNDARESANK\workspace\python-practice\user-service
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```bash
# Windows:
copy .env.example .env

# Linux/Mac:
cp .env.example .env
```

Update `.env` with your configuration:

```env
APP_NAME=User Management Service
DEBUG=True
DATABASE_URL=postgresql://postgres:Python123@localhost:5432/user_mgmt
HOST=0.0.0.0
PORT=8000
```

**Database Options:**

- **PostgreSQL**: `postgresql://username:password@host:port/database_name`
- **SQLite** (for testing): `sqlite:///./user_service.db`

### 5. Setup Database

**Option A: PostgreSQL**

1. Install PostgreSQL or run via Docker:

```bash
docker run -d \
  --name postgres_user_service \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=Python123 \
  -e POSTGRES_DB=user_mgmt \
  -p 5432:5432 \
  postgres:15
```

2. The application will create tables automatically on startup.

**Option B: SQLite (Quick Testing)**

Update `.env`:
```env
DATABASE_URL=sqlite:///./user_service.db
```

### 6. Run the Application

```bash
# Development mode with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Or using Python module
python -m uvicorn main:app --reload

# Or run directly
python main.py
```

### 7. Access the Application

- **API Documentation (Swagger)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **Root Endpoint**: http://localhost:8000/

## API Endpoints

### User Registration

**Endpoint**: `POST /api/users/register`

**Request Body**:
```json
{
  "firstname": "John",
  "lastname": "Doe",
  "email": "john.doe@example.com",
  "username": "johndoe123",
  "password": "SecurePass123!",
  "confirmpassword": "SecurePass123!",
  "countrycode": "+1",
  "mobilenumber": "1234567890"
}
```

**Validation Rules**:
- `firstname`: Alphabetic characters only, 2-50 chars
- `lastname`: Alphabetic characters only, 2-50 chars
- `email`: Valid email format
- `username`: Alphanumeric only, 3-30 chars, unique
- `password`: Min 8 chars with letters, numbers, and special chars (@$!%*#?&)
- `confirmpassword`: Must match password
- `countrycode`: Format: +{1-4 digits}
- `mobilenumber`: 10-15 digits, unique (with country code)

**Success Response (201)**:
```json
{
  "message": "User created successfully"
}
```

**Error Response (400)**:
```json
{
  "message": "Validation error",
  "errorInfo": {
    "detail": "Username already exists"
  }
}
```

## Testing

### Using Swagger UI

1. Open http://localhost:8000/docs
2. Click on `POST /api/users/register`
3. Click "Try it out"
4. Enter request body
5. Click "Execute"

### Using cURL

```bash
curl -X POST "http://localhost:8000/api/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "firstname": "John",
    "lastname": "Doe",
    "email": "john.doe@example.com",
    "username": "johndoe123",
    "password": "SecurePass123!",
    "confirmpassword": "SecurePass123!",
    "countrycode": "+1",
    "mobilenumber": "1234567890"
  }'
```

### Using Python

```python
import requests

url = "http://localhost:8000/api/users/register"
data = {
    "firstname": "John",
    "lastname": "Doe",
    "email": "john.doe@example.com",
    "username": "johndoe123",
    "password": "SecurePass123!",
    "confirmpassword": "SecurePass123!",
    "countrycode": "+1",
    "mobilenumber": "1234567890"
}

response = requests.post(url, json=data)
print(response.json())
```

## Architecture

### Layers

1. **API Layer** (`api/routes/`): HTTP endpoints and request/response handling
2. **Service Layer** (`services/`): Business logic and validation
3. **Repository Layer** (`repositories/`): Data access and database operations
4. **Model Layer** (`models/`): Database models (SQLAlchemy)
5. **Schema Layer** (`schemas/`): Request/response validation (Pydantic)

### Design Patterns

- **Repository Pattern**: Abstraction over data access
- **Service Pattern**: Business logic separation
- **Dependency Injection**: Database session management
- **Exception Handling**: Custom exceptions for different error types

## Development

### Project Dependencies

- **FastAPI**: Modern web framework
- **Uvicorn**: ASGI server
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation
- **Bcrypt**: Password hashing
- **Psycopg2**: PostgreSQL adapter

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Document classes and methods
- Keep functions focused and small

## Troubleshooting

### Port Already in Use

```bash
# Use a different port
uvicorn main:app --reload --port 8001
```

### Database Connection Error

1. Verify PostgreSQL is running
2. Check credentials in `.env`
3. Test connection manually
4. For quick testing, use SQLite

### Import Errors

Ensure you're running from the project root:
```bash
cd C:\Users\SUNDARESANK\workspace\python-practice\user-service
python -m uvicorn main:app --reload
```

### Module Not Found

```bash
# Reinstall dependencies
pip install -r requirements.txt
```

## Security Considerations

- Passwords are hashed using bcrypt
- Input validation on all fields
- SQL injection prevention via SQLAlchemy ORM
- Unique constraints on username, email, and mobile

## Future Enhancements

- [ ] JWT authentication
- [ ] User login endpoint
- [ ] Password reset functionality
- [ ] Email verification
- [ ] Rate limiting
- [ ] API versioning
- [ ] Docker compose setup
- [ ] Unit and integration tests
- [ ] CI/CD pipeline

## License

MIT License

## Contact

For questions or issues, please contact the development team.

