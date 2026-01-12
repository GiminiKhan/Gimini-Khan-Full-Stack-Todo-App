from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
import uuid

from ...database.session import get_db_session
from ...models.project import Project
from ...models.better_auth_user import BetterAuthUser
from ..schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from ..deps import get_current_better_auth_user

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/", response_model=List[ProjectResponse])
async def get_projects(
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Get all projects for the current user.
    """
    result = await db.execute(
        select(Project).where(Project.owner_id == current_user.id)
    )
    projects = result.scalars().all()
    return projects


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: uuid.UUID,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Get a specific project by ID.
    """
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.owner_id == current_user.id)
    )
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found or access denied"
        )

    return project


@router.post("/", response_model=ProjectResponse)
async def create_project(
    project_data: ProjectCreate,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Create a new project for the current user.
    """
    db_project = Project(
        title=project_data.title,
        description=project_data.description,
        owner_id=current_user.id
    )

    db.add(db_project)
    await db.commit()
    await db.refresh(db_project)

    return db_project


@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: uuid.UUID,
    project_data: ProjectUpdate,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Update a specific project.
    """
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.owner_id == current_user.id)
    )
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found or access denied"
        )

    # Update fields that are provided
    if project_data.title is not None:
        project.title = project_data.title
    if project_data.description is not None:
        project.description = project_data.description

    await db.commit()
    await db.refresh(project)

    return project


@router.delete("/{project_id}")
async def delete_project(
    project_id: uuid.UUID,
    current_user: BetterAuthUser = Depends(get_current_better_auth_user),
    db: AsyncSession = Depends(get_db_session)
):
    """
    Delete a specific project.
    """
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.owner_id == current_user.id)
    )
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found or access denied"
        )

    await db.delete(project)
    await db.commit()

    return {"message": "Project deleted successfully"}