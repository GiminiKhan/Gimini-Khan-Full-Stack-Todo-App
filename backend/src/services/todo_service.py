"""Service layer for Todo operations."""

from sqlmodel import Session, select
from typing import List, Optional
from uuid import UUID
from ..models.todo import Todo, TodoBase
from ..models.user import User
from ..core.exceptions import TodoNotFoundException, PermissionDeniedException


class TodoService:
    """Service class for handling todo-related operations."""

    def __init__(self, db_session: Session):
        """Initialize the todo service with a database session."""
        self.db_session = db_session

    def get_user_todos(self, user_id: UUID) -> List[Todo]:
        """
        Get all todos for a specific user.

        Args:
            user_id: The ID of the user whose todos to retrieve

        Returns:
            List of todos belonging to the user
        """
        statement = select(Todo).where(Todo.user_id == user_id)
        return self.db_session.exec(statement).all()

    def get_todo_by_id(self, todo_id: UUID, user_id: UUID) -> Optional[Todo]:
        """
        Get a specific todo by ID for a specific user.

        Args:
            todo_id: The ID of the todo to retrieve
            user_id: The ID of the user who owns the todo

        Returns:
            The todo if found and owned by the user, None otherwise
        """
        statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
        return self.db_session.exec(statement).first()

    def create_todo(self, todo_data: TodoBase, user_id: UUID) -> Todo:
        """
        Create a new todo for a user.

        Args:
            todo_data: The data for the new todo
            user_id: The ID of the user creating the todo

        Returns:
            The created todo
        """
        todo = Todo(**todo_data.dict(), user_id=user_id)
        self.db_session.add(todo)
        self.db_session.commit()
        self.db_session.refresh(todo)
        return todo

    def update_todo(self, todo_id: UUID, user_id: UUID, updates: TodoBase) -> Optional[Todo]:
        """
        Update a todo for a user.

        Args:
            todo_id: The ID of the todo to update
            user_id: The ID of the user who owns the todo
            updates: The updates to apply to the todo

        Returns:
            The updated todo if successful, None if not found or not owned by user
        """
        # Get the existing todo
        existing_todo = self.get_todo_by_id(todo_id, user_id)

        if not existing_todo:
            return None

        # Update the todo with the new data
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(existing_todo, key, value)

        self.db_session.add(existing_todo)
        self.db_session.commit()
        self.db_session.refresh(existing_todo)
        return existing_todo

    def delete_todo(self, todo_id: UUID, user_id: UUID) -> bool:
        """
        Delete a todo for a user.

        Args:
            todo_id: The ID of the todo to delete
            user_id: The ID of the user who owns the todo

        Returns:
            True if the todo was deleted, False if not found or not owned by user
        """
        # Get the existing todo
        existing_todo = self.get_todo_by_id(todo_id, user_id)

        if not existing_todo:
            return False

        # Delete the todo
        self.db_session.delete(existing_todo)
        self.db_session.commit()
        return True