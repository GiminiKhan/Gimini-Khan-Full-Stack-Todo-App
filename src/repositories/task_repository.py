"""
InMemoryTaskRepo - Repository for managing tasks in memory.
Implements CRUD operations for Task entities.
"""
from typing import Dict, List, Optional
from src.models.task import Task


class InMemoryTaskRepository:
    """
    Implements InMemory Repository with CRUD methods.
    Uses a dictionary for O(1) lookup by task ID.
    """
    def __init__(self):
        """Initialize the in-memory storage."""
        self._tasks: Dict[str, Task] = {}

    def add(self, task: Task) -> Task:
        """
        Add a new task to the repository.

        Args:
            task: The task to add

        Returns:
            Task: The added task
        """
        self._tasks[task.id] = task
        return task

    def get_by_id(self, task_id: str) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task: The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def list_all(self) -> List[Task]:
        """
        Retrieve all tasks.

        Returns:
            List[Task]: All tasks in the repository
        """
        return list(self._tasks.values())

    def update(self, task_id: str, title: Optional[str] = None,
               description: Optional[str] = None, status: Optional[bool] = None) -> Optional[Task]:
        """
        Update an existing task.

        Args:
            task_id: ID of the task to update
            title: New title (optional)
            description: New description (optional)
            status: New status (optional)

        Returns:
            Task: Updated task if successful, None if task doesn't exist
        """
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]

        if title is not None:
            task.title = title.strip() if title else task.title
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status

        return task

    def delete(self, task_id: str) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: ID of the task to delete

        Returns:
            bool: True if task was deleted, False if task didn't exist
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_status(self, task_id: str) -> Optional[Task]:
        """
        Toggle the status of a task.

        Args:
            task_id: ID of the task to toggle

        Returns:
            Task: Updated task if successful, None if task doesn't exist
        """
        if task_id not in self._tasks:
            return None

        task = self._tasks[task_id]
        task.toggle_status()
        return task