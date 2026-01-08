#!/usr/bin/env python3
"""
Simple test to verify that the UserResponse schema works with UUID serialization.
"""

import sys
import os
import uuid

# Add the backend directory to the path so we can import the schema
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'backend'))

from api.schemas.user import UserResponse


def test_basic_functionality():
    """Test basic functionality of the updated UserResponse schema."""
    print("Testing basic UserResponse functionality...")

    # Create a UUID
    user_id = uuid.uuid4()

    # Create a UserResponse instance
    user_response = UserResponse(
        id=user_id,
        email="test@example.com",
        full_name="Test User",
        is_active=True
    )

    print(f"  [INFO] Created UserResponse with ID: {user_response.id}")
    print(f"  [INFO] ID type: {type(user_response.id)}")
    print(f"  [INFO] Email: {user_response.email}")

    # Test model dump (this is what FastAPI uses internally)
    user_dict = user_response.model_dump()
    print(f"  [PASS] Model dump successful: {user_dict}")

    # Test JSON serialization using Pydantic's method
    json_str = user_response.model_dump_json()
    print(f"  [PASS] JSON serialization successful")

    # Parse the JSON back
    import json
    parsed = json.loads(json_str)
    print(f"  [PASS] JSON parsing successful: {parsed}")

    # Verify the ID in the parsed JSON is a string (which is what FastAPI needs)
    id_from_json = parsed['id']
    print(f"  [INFO] ID from JSON: {id_from_json}")
    print(f"  [INFO] Type of ID from JSON: {type(id_from_json)}")

    if isinstance(id_from_json, str):
        print("  [PASS] UUID properly serialized to string in JSON")
        return True
    else:
        print(f"  [FAIL] Expected string, got {type(id_from_json)}")
        return False


def test_from_attributes():
    """Test the from_attributes functionality."""
    print("\nTesting from_attributes functionality...")

    # Create a mock object with attributes (simulating a SQLAlchemy model)
    class MockUser:
        def __init__(self):
            self.id = uuid.uuid4()
            self.email = "attr_test@example.com"
            self.full_name = "Attribute Test User"
            self.is_active = True

    mock_user = MockUser()

    # Create UserResponse from attributes
    user_response = UserResponse.model_validate(mock_user)

    print(f"  [PASS] Created from attributes: {user_response}")
    print(f"  [INFO] ID from attributes: {user_response.id}")

    # Test JSON serialization
    json_str = user_response.model_dump_json()
    parsed = user_response.model_dump()

    print(f"  [PASS] From-attributes serialization works")

    # Verify the ID is properly serialized to string in JSON
    id_from_json = parsed['id']
    if isinstance(id_from_json, str):
        print("  [PASS] UUID from attributes properly serialized to string in JSON")
        return True
    else:
        print(f"  [FAIL] Expected string from attributes, got {type(id_from_json)}")
        return False


if __name__ == "__main__":
    print("Running simple UUID serialization test...\n")

    success1 = test_basic_functionality()
    success2 = test_from_attributes()

    if success1 and success2:
        print("\n[PASS] All tests passed! UUID serialization is working correctly.")
    else:
        print("\n[FAIL] Some tests failed!")
        sys.exit(1)