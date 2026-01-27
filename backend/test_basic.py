"""Basic test to verify backend functionality."""

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_endpoint():
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_auth_routes_exist():
    """Test that auth routes exist."""
    # This will return 405 (Method Not Allowed) since GET is not allowed for /auth/login
    # but if it was 404, the route wouldn't exist
    response = client.get("/auth/login")
    assert response.status_code != 404


def test_todos_routes_exist():
    """Test that todos routes exist."""
    # This will return 401 (Unauthorized) since no auth token is provided
    # but if it was 404, the route wouldn't exist
    response = client.get("/todos/")
    assert response.status_code != 404