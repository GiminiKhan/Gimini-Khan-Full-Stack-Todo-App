from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    priority: int = 2  # 1: low, 2: medium, 3: high, 4: urgent
    project_id: Optional[uuid.UUID] = None


class TodoCreate(TodoBase):
    title: str
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    priority: Optional[int] = None
    project_id: Optional[uuid.UUID] = None


class TodoResponse(TodoBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True