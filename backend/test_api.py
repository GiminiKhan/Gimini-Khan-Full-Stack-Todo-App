"""Simple test to verify the API is working."""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    print("✓ Root endpoint works:", response.json())


def test_health():
    """Test the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    print("✓ Health endpoint works:", response.json())


def test_auth_routes():
    """Test that auth routes exist."""
    # This will return 405 (Method Not Allowed) since GET is not allowed for /auth/login
    # but if it was 404, the route wouldn't exist
    response = client.get("/auth/login")
    assert response.status_code != 404
    print("✓ Auth routes exist")


def test_todos_routes():
    """Test that todos routes exist."""
    # This will return 401 (Unauthorized) since no auth token is provided
    # but if it was 404, the route wouldn't exist
    response = client.get("/todos/")
    assert response.status_code != 404
    print("✓ Todos routes exist")


if __name__ == "__main__":
    print("Testing API endpoints...")
    test_root()
    test_health()
    test_auth_routes()
    test_todos_routes()
    print("\nAll API tests passed! ✓")