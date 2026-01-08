#!/usr/bin/env python3
"""
Test script to verify that UUID serialization works correctly in the UserResponse schema.
"""

import sys
import os
import uuid
from typing import Optional

# Add the backend directory to the path so we can import the schema
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'backend'))

from api.schemas.user import UserResponse
from models.user import User


def test_uuid_serialization():
    """Test that UUID fields serialize properly in the UserResponse schema."""
    print("Testing UUID serialization in UserResponse schema...")

    # Create a mock user object similar to what would come from the database
    mock_uuid = uuid.uuid4()

    # Create a mock user object that mimics SQLAlchemy model behavior
    class MockUser:
        def __init__(self):
            self.id = mock_uuid
            self.email = "test@example.com"
            self.full_name = "Test User"
            self.is_active = True

    # Test that the schema can be created from attributes (from_attributes=True)
    try:
        user_response = UserResponse.model_validate({
            'id': mock_uuid,
            'email': 'test@example.com',
            'full_name': 'Test User',
            'is_active': True
        })

        print(f"  [PASS] Schema validation successful")
        print(f"  [INFO] User ID: {user_response.id}")
        print(f"  [INFO] User ID type: {type(user_response.id)}")
        print(f"  [INFO] Email: {user_response.email}")

        # Verify the ID can be serialized to string (for JSON response)
        id_str = str(user_response.id)
        print(f"  [PASS] ID serializes to string: {id_str}")

        return True
    except Exception as e:
        print(f"  [FAIL] Error: {e}")
        return False


def test_sqlalchemy_model_compatibility():
    """Test that the schema works with actual SQLAlchemy models."""
    print("\nTesting compatibility with SQLAlchemy User model...")

    try:
        # Create a real User model instance (this mimics what comes from the DB)
        user = User(
            email="test@example.com",
            full_name="Test User",
            hashed_password="hashed_password_here"
        )

        # Verify the user has a UUID id
        print(f"  [INFO] Created user with ID: {user.id}")
        print(f"  [INFO] User ID type: {type(user.id)}")

        # Create schema from the model using from_attributes=True
        user_response = UserResponse.model_validate(user)

        print(f"  [PASS] Schema created from model successfully")
        print(f"  [INFO] Schema ID: {user_response.id}")
        print(f"  [INFO] Schema ID type: {type(user_response.id)}")

        # Verify it can be serialized to dict (for JSON response)
        user_dict = user_response.model_dump()
        print(f"  [PASS] Schema serializes to dict successfully")
        print(f"  [INFO] Dict ID: {user_dict['id']}")

        return True
    except Exception as e:
        print(f"  [FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_json_serialization():
    """Test that the schema can be serialized to JSON."""
    print("\nTesting JSON serialization...")

    try:
        mock_uuid = uuid.uuid4()

        user_response = UserResponse(
            id=mock_uuid,
            email="test@example.com",
            full_name="Test User",
            is_active=True
        )

        # Convert to dict for JSON serialization
        user_dict = user_response.model_dump()
        print(f"  [PASS] Converted to dict: {user_dict}")

        # Test that the ID field can be converted to string
        id_as_string = str(user_dict['id'])
        print(f"  [PASS] ID can be converted to string: {id_as_string}")

        # Test that the model can be serialized to JSON using Pydantic's method
        import json
        json_str = user_response.model_dump_json()
        print(f"  [PASS] Successfully serialized to JSON using Pydantic")

        # Verify the JSON can be parsed back
        parsed = json.loads(json_str)
        print(f"  [PASS] JSON can be parsed back: {parsed}")

        return True
    except Exception as e:
        print(f"  [FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_all_tests():
    """Run all tests."""
    print("Running UUID serialization tests...\n")

    success = True
    success &= test_uuid_serialization()
    success &= test_sqlalchemy_model_compatibility()
    success &= test_json_serialization()

    if success:
        print("\n[PASS] All tests passed! UUID serialization is working correctly.")
        return True
    else:
        print("\n[FAIL] Some tests failed!")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    if not success:
        sys.exit(1)