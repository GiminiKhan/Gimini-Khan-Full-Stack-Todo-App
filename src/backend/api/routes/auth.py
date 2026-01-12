from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
import uuid

from ...database.session import get_db_session
from ...models.models import BetterAuthUser
from ..schemas.user import UserCreate, UserResponse, Token, UserLogin
from ...core.security import verify_password, get_password_hash, create_access_token
from ...core.config import settings
from ..deps import get_current_better_auth_user

router = APIRouter(tags=["Authentication"])

@router.post("/register", response_model=UserResponse)
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db_session)):
    """
    Register a new user account.
    NOTE: This endpoint is maintained for API compatibility but users should
    use Better Auth directly for authentication. This creates a reference record
    for application data purposes only.
    """
    # Check if user already exists in our reference table
    result = await db.execute(select(BetterAuthUser).filter(BetterAuthUser.email == user_data.email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists"
        )

    # Create a reference user record for our application data
    # Actual authentication is handled by Better Auth
    db_user = BetterAuthUser(
        email=user_data.email,
        name=user_data.full_name
    )

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return UserResponse(
        id=str(db_user.id),
        email=db_user.email,
        full_name=db_user.name,
        is_active=True  # User will be active once verified via Better Auth
    )


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db_session)
):
    """
    OAuth2 compatible token login, gets an access token for future requests.
    NOTE: This endpoint is maintained for API compatibility but users should
    use Better Auth directly for authentication.
    """
    # Find user in our reference table
    result = await db.execute(select(BetterAuthUser).filter(BetterAuthUser.email == form_data.username))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # For API compatibility, return a token
    # In production, you would verify the Better Auth session instead
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email, "user_id": str(user.id)}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login", response_model=Token)
async def login_user(user_data: UserLogin, db: AsyncSession = Depends(get_db_session)):
    """
    Login endpoint that returns JWT token.
    NOTE: This endpoint is maintained for API compatibility but users should
    use Better Auth directly for authentication.
    """
    # Find user in our reference table
    result = await db.execute(select(BetterAuthUser).filter(BetterAuthUser.email == user_data.email))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # For API compatibility, return a token
    # In production, you would verify the Better Auth session instead
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email, "user_id": str(user.id)}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

# Better Auth compatibility endpoints
@router.get("/me")
async def get_current_user_from_better_auth(
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Get current user info based on Better Auth session.
    This endpoint verifies the Better Auth session and returns user info.
    """
    # The user is already retrieved via the dependency
    return UserResponse(
        id=str(current_user.id),
        email=current_user.email,
        full_name=current_user.name,
        is_active=True
    )