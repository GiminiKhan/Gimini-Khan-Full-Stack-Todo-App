import sys
import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# For Vercel compatibility, we'll use relative imports
from .core.config import settings
from .api.routes.auth import router as auth_router
from .api.routes.tasks import router as tasks_router  # Updated to tasks

def create_app():
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        debug=settings.debug,
    )

    # Add CORS middleware to allow communication with Next.js frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include authentication routes
    app.include_router(auth_router, prefix="/api/auth")

    # Include tasks routes with the required format: /api/{user_id}/tasks
    app.include_router(tasks_router, prefix="/api")

    # Better Auth session verification endpoint
    @app.get("/api/auth/session")
    async def get_session(request: Request):
        """
        Better Auth session endpoint.
        This endpoint is used by the frontend to check session status.
        """
        from .services.better_auth_service import better_auth_service

        # Extract token from Authorization header
        authorization = request.headers.get("authorization")
        if authorization and authorization.startswith("Bearer "):
            token = authorization.split(" ")[1]

            # Verify the Better Auth session
            user_info = await better_auth_service.verify_session(token)

            if user_info:
                return {
                    "user": {
                        "id": user_info.get("id"),
                        "email": user_info.get("email"),
                        "name": user_info.get("name"),
                        "email_verified": user_info.get("email_verified", False)
                    },
                    "status": "authenticated"
                }

        return {"user": None, "status": "unauthenticated"}

    @app.get("/")
    async def root():
        return {"message": "Welcome to the To-Do App API"}

    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "database_url": settings.database_url}

    return app

app = create_app()