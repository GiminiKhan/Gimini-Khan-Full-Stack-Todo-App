from fastapi import FastAPI
from .core.config import settings
from .api.routes.auth import router as auth_router
from .api.routes.projects import router as projects_router
from .api.routes.todos import router as todos_router


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
