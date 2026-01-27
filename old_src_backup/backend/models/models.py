from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid


class BetterAuthUser(SQLModel, table=True):
    """
    Better Auth User model that connects to the Better Auth managed user table.
    This model allows our application to reference Better Auth users for our own data.
    """
    __tablename__ = "better_auth_users"  # This will be managed by Better Auth

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(sa_column_kwargs={"unique": True, "nullable": False})
    email_verified: bool = Field(default=False)
    name: Optional[str] = Field(default=None)
    username: Optional[str] = Field(sa_column_kwargs={"unique": True})
    locale: Optional[str] = Field(default=None)
    image: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    # Relationships to our application data
    projects: List["Project"] = Relationship(back_populates="owner", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    todos: List["Todo"] = Relationship(back_populates="owner", sa_relationship_kwargs={"cascade": "all, delete-orphan"})


class Project(SQLModel, table=True):
    __tablename__ = "projects"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255, nullable=False)
    description: Optional[str] = Field(default=None, max_length=1000)
    owner_id: uuid.UUID = Field(foreign_key="better_auth_users.id", nullable=False)

    # Relationships
    owner: BetterAuthUser = Relationship(back_populates="projects")
    todos: List["Todo"] = Relationship(back_populates="project")


class Todo(SQLModel, table=True):
    __tablename__ = "todos"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str = Field(max_length=255, nullable=False)
    description: Optional[str] = Field(default=None, max_length=1000)
    is_completed: bool = Field(default=False)
    priority: int = Field(default=1)  # 1: low, 2: medium, 3: high, 4: urgent
    owner_id: uuid.UUID = Field(foreign_key="better_auth_users.id", nullable=False)
    project_id: Optional[uuid.UUID] = Field(default=None, foreign_key="projects.id")

    # Relationships
    owner: BetterAuthUser = Relationship(back_populates="todos")
    project: Optional[Project] = Relationship(back_populates="todos")

    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)