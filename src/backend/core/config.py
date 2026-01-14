from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    # Database settings
    database_url: Optional[str] = None

    # Application settings
    app_name: str = "To-Do App API"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    version: str = "0.1.0"

    # JWT settings
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Better Auth settings
    better_auth_secret: Optional[str] = os.getenv("BETTER_AUTH_SECRET")
    better_auth_url: Optional[str] = os.getenv("BETTER_AUTH_URL", "http://localhost:3000")

    # CORS settings
    allowed_origins: list[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:8000",
        "https://vercel.app",  # Vercel preview deployments
        os.getenv("FRONTEND_URL", "https://your-frontend-url.vercel.app")  # Production frontend
    ]

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
        env_file_encoding = 'utf-8'
        case_sensitive = True
        extra = "allow"  # Allow extra fields from alembic


# Create a single instance of settings
settings = Settings()