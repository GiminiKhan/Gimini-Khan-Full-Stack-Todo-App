"""Initialize database tables."""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from sqlmodel import SQLModel
from src.core.database import engine
from src.models.user import User
from src.models.todo import Todo


def create_tables():
    """Create all database tables."""
    print("Creating database tables...")
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    create_tables()