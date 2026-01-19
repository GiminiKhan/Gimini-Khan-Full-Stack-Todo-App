from fastapi import APIRouter, Depends, HTTPException, status, Path, Query
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from typing import List, Optional
import uuid

from src.backend.database.session import get_db_session
from src.backend.models.models import Todo, BetterAuthUser, Project
from src.backend.api.schemas.todo import TodoCreate, TodoUpdate, TodoResponse  # Using existing schema
from src.backend.api.deps import get_current_better_auth_user

router = APIRouter(prefix="", tags=["Tasks"])  # Empty prefix since we'll define full paths


@router.get("/api/{user_id}/tasks", response_model=List[TodoResponse])
async def get_tasks(
    user_id: uuid.UUID,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session),
    project_id: Optional[uuid.UUID] = Query(None, description="Filter tasks by project ID"),
    is_completed: Optional[bool] = Query(None, description="Filter by completion status"),
    priority: Optional[int] = Query(None, description="Filter by priority level")
):
    """
    Get all tasks for a specific user, with optional filtering.
    The user_id in the path must match the authenticated user.
    """
    # Verify that the requested user_id matches the authenticated user
    if str(current_user.id) != str(user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access another user's tasks"
        )

    query = select(Todo).where(Todo.owner_id == current_user.id)

    if project_id is not None:
        query = query.where(Todo.project_id == project_id)
    if is_completed is not None:
        query = query.where(Todo.is_completed == is_completed)
    if priority is not None:
        query = query.where(Todo.priority == priority)

    result = await db.execute(query)
    tasks = result.scalars().all()
    return tasks


@router.get("/api/{user_id}/tasks/{task_id}", response_model=TodoResponse)
async def get_task(
    user_id: uuid.UUID,
    task_id: uuid.UUID,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Get a specific task by ID for a user.
    The user_id in the path must match the authenticated user.
    """
    # Verify that the requested user_id matches the authenticated user
    if str(current_user.id) != str(user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access another user's tasks"
        )

    result = await db.execute(
        select(Todo).where(Todo.id == task_id, Todo.owner_id == current_user.id)
    )
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )

    return task


@router.post("/api/{user_id}/tasks", response_model=TodoResponse)
async def create_task(
    user_id: uuid.UUID,
    task_data: TodoCreate,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Create a new task for a specific user.
    The user_id in the path must match the authenticated user.
    """
    # Verify that the requested user_id matches the authenticated user
    if str(current_user.id) != str(user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot create tasks for another user"
        )

    # Check if project exists and belongs to user
    if task_data.project_id is not None:
        project_result = await db.execute(
            select(Project).where(Project.id == task_data.project_id, Project.owner_id == current_user.id)
        )
        project = project_result.scalar_one_or_none()
        if not project:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project not found or access denied"
            )

    db_task = Todo(
        title=task_data.title,
        description=task_data.description,
        is_completed=task_data.is_completed,
        priority=task_data.priority,
        owner_id=current_user.id,
        project_id=task_data.project_id
    )

    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)

    return db_task


@router.put("/api/{user_id}/tasks/{task_id}", response_model=TodoResponse)
async def update_task(
    user_id: uuid.UUID,
    task_id: uuid.UUID,
    task_data: TodoUpdate,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Update a specific task for a user.
    The user_id in the path must match the authenticated user.
    """
    # Verify that the requested user_id matches the authenticated user
    if str(current_user.id) != str(user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot update another user's tasks"
        )

    result = await db.execute(
        select(Todo).where(Todo.id == task_id, Todo.owner_id == current_user.id)
    )
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )

    # Check if project exists and belongs to user when updating project_id
    if task_data.project_id is not None:
        project_result = await db.execute(
            select(Project).where(Project.id == task_data.project_id, Project.owner_id == current_user.id)
        )
        project = project_result.scalar_one_or_none()
        if not project:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project not found or access denied"
            )

    # Update fields that are provided
    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.is_completed is not None:
        task.is_completed = task_data.is_completed
    if task_data.priority is not None:
        task.priority = task_data.priority
    if task_data.project_id is not None:
        task.project_id = task_data.project_id

    await db.commit()
    await db.refresh(task)

    return task


@router.patch("/api/{user_id}/tasks/{task_id}/complete", response_model=TodoResponse)
async def update_task_completion(
    user_id: uuid.UUID,
    task_id: uuid.UUID,
    is_completed: bool = Query(default=True, description="Set task completion status"),
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Update the completion status of a specific task for a user.
    The user_id in the path must match the authenticated user.
    """
    # Verify that the requested user_id matches the authenticated user
    if str(current_user.id) != str(user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot update another user's tasks"
        )

    result = await db.execute(
        select(Todo).where(Todo.id == task_id, Todo.owner_id == current_user.id)
    )
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )

    task.is_completed = is_completed
    await db.commit()
    await db.refresh(task)

    return task


@router.delete("/api/{user_id}/tasks/{task_id}")
async def delete_task(
    user_id: uuid.UUID,
    task_id: uuid.UUID,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Delete a specific task for a user.
    The user_id in the path must match the authenticated user.
    """
    # Verify that the requested user_id matches the authenticated user
    if str(current_user.id) != str(user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot delete another user's tasks"
        )

    result = await db.execute(
        select(Todo).where(Todo.id == task_id, Todo.owner_id == current_user.id)
    )
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or access denied"
        )

    await db.delete(task)
    await db.commit()

    return {"message": "Task deleted successfully"}