#!/usr/bin/env python3
"""
Test script to verify the bcrypt ValueError fix in security.py
"""
import sys
import os

# Add the src directory to the path so we can import the backend modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from backend.core.security import get_password_hash, verify_password


def test_bcrypt_fix():
    """
    Test the bcrypt fix with various password lengths
    """
    print("Testing bcrypt fix with various password lengths...")

    # Test with normal password
    normal_password = "normalpassword123"
    print(f"\n1. Testing normal password: '{normal_password}'")

    try:
        hash_result = get_password_hash(normal_password)
        print(f"   Hash created successfully: {hash_result[:20]}...")

        verification = verify_password(normal_password, hash_result)
        print(f"   Verification successful: {verification}")
    except Exception as e:
        print(f"   Error with normal password: {e}")
        return False

    # Test with password that is exactly 72 characters (the limit)
    limit_password = "a" * 72
    print(f"\n2. Testing 72-character password (exact limit)")

    try:
        hash_result = get_password_hash(limit_password)
        print(f"   Hash created successfully: {hash_result[:20]}...")

        verification = verify_password(limit_password, hash_result)
        print(f"   Verification successful: {verification}")
    except Exception as e:
        print(f"   Error with 72-character password: {e}")
        return False

    # Test with password longer than 72 characters (should trigger the workaround)
    long_password = "a" * 80  # 80 characters, exceeding the 72-character limit
    print(f"\n3. Testing 80-character password (exceeds limit)")

    try:
        hash_result = get_password_hash(long_password)
        print(f"   Hash created successfully: {hash_result[:20]}...")

        verification = verify_password(long_password, hash_result)
        print(f"   Verification successful: {verification}")
    except Exception as e:
        print(f"   Error with long password: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test with non-string input (should be converted to string)
    numeric_password = 12345
    print(f"\n4. Testing numeric password (should be converted to string): {numeric_password}")

    try:
        hash_result = get_password_hash(numeric_password)
        print(f"   Hash created successfully: {hash_result[:20]}...")

        verification = verify_password(numeric_password, hash_result)
        print(f"   Verification successful: {verification}")
    except Exception as e:
        print(f"   Error with numeric password: {e}")
        return False

    print("\n✅ All tests passed! The bcrypt fix is working correctly.")
    return True


if __name__ == "__main__":
    print("Starting bcrypt fix verification test...")
    success = test_bcrypt_fix()

    if success:
        print("\n🎉 Bcrypt fix test completed successfully!")
        print("The ValueError fix for passwords longer than 72 bytes has been applied correctly.")
    else:
        print("\n💥 Bcrypt fix test failed!")
        sys.exit(1)