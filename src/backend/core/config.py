from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
print(f"DEBUG: Loaded DATABASE_URL: {os.getenv('DATABASE_URL')}")


class Settings(BaseSettings):
    # Database settings
    database_url: Optional[str] = None

    # Application settings
    app_name: str = "To-Do App API"
    debug: bool = False
    version: str = "0.1.0"

    # JWT settings
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Better Auth settings
    better_auth_secret: Optional[str] = None
    better_auth_url: Optional[str] = None

    # CORS settings
    allowed_origins: list[str] = ["http://localhost:3000", "http://localhost:3001", "http://localhost:8000"]

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
        env_file_encoding = 'utf-8'
        case_sensitive = True
        extra = "allow"  # Allow extra fields from alembic


# Create a single instance of settings
settings = Settings()