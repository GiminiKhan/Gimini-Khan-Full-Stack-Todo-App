from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from typing import List, Optional
import uuid

from ...database.session import get_db_session
from ...models.todo import Todo
from ...models.better_auth_user import BetterAuthUser
from ...models.project import Project
from ..schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from ..deps import get_current_better_auth_user

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", response_model=List[TodoResponse])
async def get_todos(
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session),
    project_id: Optional[uuid.UUID] = Query(None, description="Filter todos by project ID"),
    is_completed: Optional[bool] = Query(None, description="Filter by completion status"),
    priority: Optional[int] = Query(None, description="Filter by priority level")
):
    """
    Get all todos for the current user, with optional filtering.
    """
    query = select(Todo).where(Todo.owner_id == current_user.id)

    if project_id is not None:
        query = query.where(Todo.project_id == project_id)
    if is_completed is not None:
        query = query.where(Todo.is_completed == is_completed)
    if priority is not None:
        query = query.where(Todo.priority == priority)

    result = await db.execute(query)
    todos = result.scalars().all()
    return todos


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(
    todo_id: uuid.UUID,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Get a specific todo by ID.
    """
    result = await db.execute(
        select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    )
    todo = result.scalar_one_or_none()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or access denied"
        )

    return todo


@router.post("/", response_model=TodoResponse)
async def create_todo(
    todo_data: TodoCreate,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Create a new todo for the current user.
    """
    # Check if project exists and belongs to user
    if todo_data.project_id is not None:
        project_result = await db.execute(
            select(Project).where(Project.id == todo_data.project_id, Project.owner_id == current_user.id)
        )
        project = project_result.scalar_one_or_none()
        if not project:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project not found or access denied"
            )

    db_todo = Todo(
        title=todo_data.title,
        description=todo_data.description,
        is_completed=todo_data.is_completed,
        priority=todo_data.priority,
        owner_id=current_user.id,
        project_id=todo_data.project_id
    )

    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)

    return db_todo


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: uuid.UUID,
    todo_data: TodoUpdate,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Update a specific todo.
    """
    result = await db.execute(
        select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    )
    todo = result.scalar_one_or_none()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or access denied"
        )

    # Check if project exists and belongs to user when updating project_id
    if todo_data.project_id is not None:
        project_result = await db.execute(
            select(Project).where(Project.id == todo_data.project_id, Project.owner_id == current_user.id)
        )
        project = project_result.scalar_one_or_none()
        if not project:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Project not found or access denied"
            )

    # Update fields that are provided
    if todo_data.title is not None:
        todo.title = todo_data.title
    if todo_data.description is not None:
        todo.description = todo_data.description
    if todo_data.is_completed is not None:
        todo.is_completed = todo_data.is_completed
    if todo_data.priority is not None:
        todo.priority = todo_data.priority
    if todo_data.project_id is not None:
        todo.project_id = todo_data.project_id

    await db.commit()
    await db.refresh(todo)

    return todo


@router.patch("/{todo_id}/complete", response_model=TodoResponse)
async def update_todo_completion(
    todo_id: uuid.UUID,
    is_completed: bool = True,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Update the completion status of a specific todo.
    """
    result = await db.execute(
        select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    )
    todo = result.scalar_one_or_none()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or access denied"
        )

    todo.is_completed = is_completed
    await db.commit()
    await db.refresh(todo)

    return todo


@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: uuid.UUID,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Delete a specific todo.
    """
    result = await db.execute(
        select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)
    )
    todo = result.scalar_one_or_none()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or access denied"
        )

    await db.delete(todo)
    await db.commit()

    return {"message": "Todo deleted successfully"}