from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from jose import JWTError

from src.backend.database.session import get_db_session
from src.backend.models.models import BetterAuthUser
from src.backend.models.user import User
from src.backend.core.security import decode_access_token
from src.backend.core.config import settings
from src.backend.services.better_auth_service import better_auth_service


security = HTTPBearer()
better_auth_security = HTTPBearer(scheme_name="BetterAuth")


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db_session)
) -> User:
    """
    Dependency to get the current authenticated user from legacy JWT token.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token = credentials.credentials
        payload = decode_access_token(token)
        if payload is None:
            raise credentials_exception
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # Query the legacy user from the database using SQLModel
    statement = select(User).where(User.email == email)
    result = await db.execute(statement)
    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )

    return user


async def get_current_better_auth_user(
    credentials: HTTPAuthorizationCredentials = Depends(better_auth_security),
    db: AsyncSession = Depends(get_db_session)
) -> BetterAuthUser:
    """
    Dependency to get the current authenticated user from Better Auth session token.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate Better Auth credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token = credentials.credentials
        # Use the Better Auth service to verify the session
        user_info = await better_auth_service.verify_session(token)

        if not user_info:
            raise credentials_exception

        # Get the user ID from the verified session
        user_id_str = user_info.get("id")
        if not user_id_str:
            raise credentials_exception

        from uuid import UUID
        try:
            user_id = UUID(user_id_str)
            # Query the BetterAuthUser from the database using SQLModel
            statement = select(BetterAuthUser).where(BetterAuthUser.id == user_id)
            result = await db.execute(statement)
            user = result.scalar_one_or_none()

            if user is None:
                # If user doesn't exist in our reference table, create one
                # This would happen when a user signs in via Better Auth for the first time
                email = user_info.get("email")
                name = user_info.get("name")

                user = BetterAuthUser(
                    id=user_id,
                    email=email,
                    name=name
                )
                db.add(user)
                await db.commit()
                await db.refresh(user)

            return user
        except ValueError:
            # Invalid UUID format
            raise credentials_exception

    except Exception as e:
        # Log the error in real implementation
        raise credentials_exception