"""SQLModel for Todo entity."""

from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid
from typing import Optional


class TodoBase(SQLModel):
    """Base model for Todo with shared attributes."""
    title: str = Field(nullable=False, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    priority: str = Field(default="medium", max_length=20)  # "high", "medium", "low"
    completed: bool = Field(default=False)


class Todo(TodoBase, table=True):
    """Todo model with database table configuration."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)