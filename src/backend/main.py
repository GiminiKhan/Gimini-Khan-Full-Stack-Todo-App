import sys
import os
from fastapi import FastAPI

# Vercel fix: Ye lines project root ko Python path mein add karti hain
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

# Ab hum absolute imports use kar sakte hain
from src.backend.core.config import settings
from src.backend.api.routes.auth import router as auth_router
from src.backend.api.routes.projects import router as projects_router
from src.backend.api.routes.todos import router as todos_router

def create_app():
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        debug=settings.debug,
    )

    # Include authentication routes
    app.include_router(auth_router, prefix="/api/v1")

    # Include projects and todos routes
    app.include_router(projects_router, prefix="/api/v1")
    app.include_router(todos_router, prefix="/api/v1")

    @app.get("/")
    async def root():
        return {"message": "Welcome to the To-Do App API"}

    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "database_url": settings.database_url}

    return app

app = create_app()