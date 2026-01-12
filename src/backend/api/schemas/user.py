from pydantic import BaseModel
from pydantic.config import ConfigDict
from pydantic import field_serializer
from typing import Optional
from uuid import UUID


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    full_name: Optional[str] = None


class UserResponse(UserBase):
    id: UUID | str
    full_name: Optional[str] = None
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)

    @field_serializer('id')
    def serialize_id(self, value: UUID) -> str:
        return str(value)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str