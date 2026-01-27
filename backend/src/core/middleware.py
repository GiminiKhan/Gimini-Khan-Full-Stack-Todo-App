"""Middleware configuration for the application."""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .config import settings


def setup_middleware(app: FastAPI):
    """Configure middleware for the application."""

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS.split(",") if settings.BACKEND_CORS_ORIGINS != "*" else ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        # Additional security headers can be added here
    )

    # Additional middleware can be added here
    # For example: authentication middleware, logging middleware, etc.