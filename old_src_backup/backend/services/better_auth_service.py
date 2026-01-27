"""
Service to handle Better Auth integration and session verification.
"""
import httpx
from typing import Optional, Dict, Any
from jose import jwt
from src.backend.core.config import settings


class BetterAuthService:
    """
    Service class to handle Better Auth integration.
    This service provides methods to verify Better Auth sessions and
    interact with the Better Auth API when needed.
    """

    def __init__(self):
        self.base_url = settings.better_auth_url or "http://localhost:3000"
        self.secret = settings.better_auth_secret or settings.secret_key

    async def verify_session(self, session_token: str) -> Optional[Dict[str, Any]]:
        """
        Verify a Better Auth session token.

        Args:
            session_token: The session token to verify

        Returns:
            User information if valid, None if invalid
        """
        # In a real implementation, you would call Better Auth's API to verify the session
        # For now, we'll implement a proper JWT verification using Better Auth's secret
        try:
            # Decode the JWT token using Better Auth's secret
            payload = jwt.decode(
                session_token,
                self.secret,
                algorithms=["HS256"],  # Better Auth typically uses HS256
                options={"verify_exp": True}  # Verify expiration
            )

            # Extract user information from the payload
            return {
                "id": payload.get("userId") or payload.get("sub") or payload.get("user_id"),
                "email": payload.get("email"),
                "name": payload.get("name"),
                "email_verified": payload.get("emailVerified", payload.get("email_verified", False))
            }
        except jwt.ExpiredSignatureError:
            # Token has expired
            return None
        except jwt.JWTError:
            # Invalid token
            return None
        except Exception:
            # Other errors
            return None

    async def get_user_by_session(self, session_token: str) -> Optional[Dict[str, Any]]:
        """
        Get user information based on session token.

        Args:
            session_token: The session token to use for lookup

        Returns:
            User information if found and valid, None otherwise
        """
        return await self.verify_session(session_token)


# Global instance
better_auth_service = BetterAuthService()