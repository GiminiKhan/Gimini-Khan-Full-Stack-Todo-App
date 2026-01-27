from fastapi import APIRouter, Depends, HTTPException, status, Body
from typing import Dict, Any
from pydantic import BaseModel
from sqlmodel import Session
from ..core.database import get_session
from ..services.auth_service import AuthService
from ..models.user import User

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    name: str
    password: str

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/login')
async def login(data: LoginRequest, db: Session = Depends(get_session)):
    auth_service = AuthService(db)
    try:
        return auth_service.authenticate_user(data.email, data.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post('/register')
async def register(data: RegisterRequest, db: Session = Depends(get_session)):
    auth_service = AuthService(db)
    try:
        user = auth_service.register_user(data.email, data.name, data.password)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))