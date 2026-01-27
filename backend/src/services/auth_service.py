from sqlmodel import Session, select
from ..models.user import User
from ..core.security import create_access_token
import uuid

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def authenticate_user(self, email: str, password: str):
        statement = select(User).where(User.email == email)
        user = self.db.exec(statement).first()
        if not user or user.hashed_password != password: # Note: In production use hashing
            raise Exception('Invalid email or password')

        # Create JWT token with user information
        token_data = {
            "sub": str(user.id),
            "email": user.email,
            "name": user.name
        }
        access_token = create_access_token(data=token_data)

        return {
            'access_token': access_token,
            'token_type': 'bearer',
            'user': user
        }

    def register_user(self, email: str, name: str, password: str):
        user = User(email=email, name=name, hashed_password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user