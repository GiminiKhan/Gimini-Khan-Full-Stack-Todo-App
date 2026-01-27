"""Todos API endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session, select
from datetime import datetime
import uuid

from ..models.todo import Todo, TodoBase
from ..models.user import User
from .deps import get_current_user
from ..core.database import get_session
from ..core.exceptions import TodoNotFoundException, PermissionDeniedException

router = APIRouter(prefix="/api", tags=["tasks"])


@router.get("/{user_id}/tasks", response_model=List[Todo])
async def get_tasks(
    user_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
) -> List[Todo]:
    """
    Get all tasks for the specified user.

    Args:
        user_id: The ID of the user whose tasks to retrieve
        current_user: The current authenticated user
        db: Database session

    Returns:
        List of tasks for the specified user
    """
    # Validate that the requested user_id matches the authenticated user's ID
    if user_id != str(current_user.id):
        raise PermissionDeniedException(detail="Not authorized to access tasks for this user")

    # Query tasks for the current user only
    statement = select(Todo).where(Todo.user_id == current_user.id)
    tasks = db.exec(statement).all()

    return tasks


@router.post("/{user_id}/tasks", response_model=Todo)
async def create_task(
    user_id: str,
    todo_data: TodoBase,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
) -> Todo:
    """
    Create a new task for the specified user.

    Args:
        user_id: The ID of the user for whom to create the task
        todo_data: Task data from request body
        current_user: The current authenticated user
        db: Database session

    Returns:
        The created task
    """
    # Validate that the requested user_id matches the authenticated user's ID
    if user_id != str(current_user.id):
        raise PermissionDeniedException(detail="Not authorized to create tasks for this user")

    # Create new task with the current user's ID
    task = Todo(**todo_data.dict(), user_id=current_user.id)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.get("/{user_id}/tasks/{task_id}", response_model=Todo)
async def get_task(
    user_id: str,
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
) -> Todo:
    """
    Get a specific task by ID for the specified user.

    Args:
        user_id: The ID of the user whose task to retrieve
        task_id: The ID of the task to retrieve
        current_user: The current authenticated user
        db: Database session

    Returns:
        The requested task
    """
    # Validate that the requested user_id matches the authenticated user's ID
    if user_id != str(current_user.id):
        raise PermissionDeniedException(detail="Not authorized to access tasks for this user")

    # Convert task_id string to UUID object
    try:
        task_uuid = uuid.UUID(task_id)
    except ValueError:
        raise TodoNotFoundException()

    # Get the task by ID
    statement = select(Todo).where(Todo.id == task_uuid)
    task = db.exec(statement).first()

    if not task:
        raise TodoNotFoundException()

    # Check if the task belongs to the current user
    if task.user_id != current_user.id:
        raise PermissionDeniedException(detail="Not authorized to access this task")

    return task


@router.put("/{user_id}/tasks/{task_id}", response_model=Todo)
async def update_task_put(
    user_id: str,
    task_id: str,
    todo_update: TodoBase,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
) -> Todo:
    """
    Update a specific task by ID for the specified user using PUT method.

    Args:
        user_id: The ID of the user whose task to update
        task_id: The ID of the task to update
        todo_update: Updated task data from request body
        current_user: The current authenticated user
        db: Database session

    Returns:
        The updated task
    """
    # Validate that the requested user_id matches the authenticated user's ID
    if user_id != str(current_user.id):
        raise PermissionDeniedException(detail="Not authorized to update tasks for this user")

    # Convert task_id string to UUID object
    try:
        task_uuid = uuid.UUID(task_id)
    except ValueError:
        raise TodoNotFoundException()

    # Get the existing task
    statement = select(Todo).where(Todo.id == task_uuid)
    task = db.exec(statement).first()

    if not task:
        raise TodoNotFoundException()

    # Check if the task belongs to the current user
    if task.user_id != current_user.id:
        raise PermissionDeniedException(detail="Not authorized to update this task")

    # Update the task with the new data
    for key, value in todo_update.dict().items():  # Use dict() instead of exclude_unset=True for PUT
        setattr(task, key, value)
    task.updated_at = datetime.utcnow()  # Update timestamp

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.patch("/{user_id}/tasks/{task_id}", response_model=Todo)
async def update_task(
    user_id: str,
    task_id: str,
    todo_update: TodoBase,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
) -> Todo:
    """
    Update a specific task by ID for the specified user using PATCH method.

    Args:
        user_id: The ID of the user whose task to update
        task_id: The ID of the task to update
        todo_update: Updated task data from request body
        current_user: The current authenticated user
        db: Database session

    Returns:
        The updated task
    """
    # Validate that the requested user_id matches the authenticated user's ID
    if user_id != str(current_user.id):
        raise PermissionDeniedException(detail="Not authorized to update tasks for this user")

    # Convert task_id string to UUID object
    try:
        task_uuid = uuid.UUID(task_id)
    except ValueError:
        raise TodoNotFoundException()

    # Get the existing task
    statement = select(Todo).where(Todo.id == task_uuid)
    task = db.exec(statement).first()

    if not task:
        raise TodoNotFoundException()

    # Check if the task belongs to the current user
    if task.user_id != current_user.id:
        raise PermissionDeniedException(detail="Not authorized to update this task")

    # Update the task with the new data
    for key, value in todo_update.dict(exclude_unset=True).items():
        setattr(task, key, value)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.patch("/{user_id}/tasks/{task_id}/complete", response_model=Todo)
async def toggle_task_completion(
    user_id: str,
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
) -> Todo:
    """
    Toggle the completion status of a specific task by ID for the specified user.

    Args:
        user_id: The ID of the user whose task to update
        task_id: The ID of the task to toggle completion status
        current_user: The current authenticated user
        db: Database session

    Returns:
        The updated task with toggled completion status
    """
    # Validate that the requested user_id matches the authenticated user's ID
    if user_id != str(current_user.id):
        raise PermissionDeniedException(detail="Not authorized to update tasks for this user")

    # Convert task_id string to UUID object
    try:
        task_uuid = uuid.UUID(task_id)
    except ValueError:
        raise TodoNotFoundException()

    # Get the existing task
    statement = select(Todo).where(Todo.id == task_uuid)
    task = db.exec(statement).first()

    if not task:
        raise TodoNotFoundException()

    # Check if the task belongs to the current user
    if task.user_id != current_user.id:
        raise PermissionDeniedException(detail="Not authorized to update this task")

    # Toggle the completion status
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.delete("/{user_id}/tasks/{task_id}")
async def delete_task(
    user_id: str,
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_session)
) -> dict:
    """
    Delete a specific task by ID for the specified user.

    Args:
        user_id: The ID of the user whose task to delete
        task_id: The ID of the task to delete
        current_user: The current authenticated user
        db: Database session

    Returns:
        Success message
    """
    # Validate that the requested user_id matches the authenticated user's ID
    if user_id != str(current_user.id):
        raise PermissionDeniedException(detail="Not authorized to delete tasks for this user")

    # Convert task_id string to UUID object
    try:
        task_uuid = uuid.UUID(task_id)
    except ValueError:
        raise TodoNotFoundException()

    # Get the existing task
    statement = select(Todo).where(Todo.id == task_uuid)
    task = db.exec(statement).first()

    if not task:
        raise TodoNotFoundException()

    # Check if the task belongs to the current user
    if task.user_id != current_user.id:
        raise PermissionDeniedException(detail="Not authorized to delete this task")

    # Delete the task
    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}