"""SQLModel for User entity."""

from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid


class UserBase(SQLModel):
    """Base model for User with shared attributes."""
    email: str = Field(unique=True, nullable=False, max_length=255)
    name: str = Field(nullable=False, min_length=1, max_length=100)


class User(UserBase, table=True):
    """User model with database table configuration."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Hashed password would be stored here in a real implementation
    hashed_password: str = Field(nullable=False)