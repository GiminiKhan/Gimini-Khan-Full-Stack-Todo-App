"""Custom exception definitions for the application."""

from fastapi import HTTPException, status


class UserNotFoundException(HTTPException):
    """Raised when a user is not found in the database."""

    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class TodoNotFoundException(HTTPException):
    """Raised when a todo item is not found in the database."""

    def __init__(self, detail: str = "Todo not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class InvalidCredentialsException(HTTPException):
    """Raised when invalid credentials are provided during authentication."""

    def __init__(self, detail: str = "Invalid credentials"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"},
        )


class PermissionDeniedException(HTTPException):
    """Raised when a user doesn't have permission to access a resource."""

    def __init__(self, detail: str = "Permission denied"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


class DatabaseConnectionException(Exception):
    """Raised when there's an issue connecting to the database."""

    def __init__(self, detail: str = "Database connection failed"):
        self.detail = detail
        super().__init__(self.detail)


class ValidationError(Exception):
    """Raised when validation fails for business logic reasons."""

    def __init__(self, detail: str = "Validation failed"):
        self.detail = detail
        super().__init__(self.detail)