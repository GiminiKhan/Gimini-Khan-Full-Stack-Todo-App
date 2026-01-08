from datetime import datetime, timedelta
from typing import Optional
import secrets
import bcrypt

from jose import JWTError, jwt

from .config import settings

# Create JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)  # Default 15 minutes

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    # Apply the same workaround for bcrypt 72-character limit
    import hashlib

    # Ensure password is in string format
    if not isinstance(plain_password, str):
        plain_password = str(plain_password)

    # Check if password length exceeds bcrypt's 72-byte limit
    if len(plain_password.encode('utf-8')) > 72:
        # Hash the password with SHA-256 first to reduce length (same as in get_password_hash)
        plain_password = hashlib.sha256(plain_password.encode('utf-8')).hexdigest()

    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def get_password_hash(password: str) -> str:
    """Hash a password using bcrypt."""
    # bcrypt has a maximum password length of 72 bytes
    # If password is longer, we hash it with SHA-256 first to reduce length
    import hashlib

    # Ensure password is in string format
    if not isinstance(password, str):
        password = str(password)

    # Check if password length exceeds bcrypt's 72-byte limit
    if len(password.encode('utf-8')) > 72:
        # Hash the password with SHA-256 first to reduce length
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def decode_access_token(token: str) -> Optional[dict]:
    """Decode a JWT token and return the payload if valid."""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None


def generate_verification_token() -> str:
    """Generate a random verification token."""
    return secrets.token_urlsafe(32)


def generate_reset_token() -> str:
    """Generate a random password reset token."""
    return secrets.token_urlsafe(32)