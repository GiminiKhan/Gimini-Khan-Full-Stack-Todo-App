"""
Task model representing a single task with properties for management and tracking.
"""
from dataclasses import dataclass
from typing import Optional
from uuid import uuid4


@dataclass
class Task:
    """
    Represents a single task with properties for management and tracking.

    Fields:
    - id: UUID string (unique identifier, generated automatically)
    - title: String (task title, required)
    - description: String (task description, optional)
    - status: Boolean (task completion status, default: False for incomplete)
    """
    id: str
    title: str
    description: Optional[str] = None
    status: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title must not be empty or contain only whitespace")

    @classmethod
    def create(cls, title: str, description: Optional[str] = None) -> 'Task':
        """
        Create a new task with a generated UUID.

        Args:
            title: Task title (required)
            description: Task description (optional)

        Returns:
            Task: A new Task instance with generated ID and default status
        """
        return cls(
            id=str(uuid4()),
            title=title.strip(),
            description=description,
            status=False  # Default to incomplete
        )

    def mark_complete(self) -> None:
        """Mark the task as complete."""
        self.status = True

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.status = False

    def toggle_status(self) -> None:
        """Toggle the task's completion status."""
        self.status = not self.status