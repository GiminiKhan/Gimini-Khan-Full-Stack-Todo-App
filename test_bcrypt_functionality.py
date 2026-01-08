#!/usr/bin/env python3
"""
Test script to verify that the bcrypt implementation works correctly
after switching from Passlib to direct bcrypt usage.
"""

import sys
import os

# Add the backend directory to the path so we can import the security module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'backend'))

from core.security import get_password_hash, verify_password

def test_password_functions():
    """Test the password hashing and verification functions."""
    print("Testing password hashing and verification functions...")

    # Test passwords of various lengths
    test_passwords = [
        "simple",
        "password123",
        "This is a longer password with more characters!",
        "A" * 50,  # Long password
        "A" * 80,  # Very long password that exceeds bcrypt's 72-byte limit
    ]

    for i, password in enumerate(test_passwords):
        print(f"\nTest {i+1}: Password length = {len(password.encode('utf-8'))} bytes")

        # Hash the password
        hashed = get_password_hash(password)
        print(f"  Original: {password[:20]}{'...' if len(password) > 20 else ''}")
        print(f"  Hashed: {hashed[:30]}...")

        # Verify the password
        is_valid = verify_password(password, hashed)
        print(f"  Verification: {'[PASS]' if is_valid else '[FAIL]'}")

        # Test with wrong password
        wrong_verification = verify_password("wrong_password", hashed)
        print(f"  Wrong password verification: {'[PASS] (should be False)' if not wrong_verification else '[FAIL] (should be False)'}")

        if not is_valid or wrong_verification:
            print(f"  ERROR: Test {i+1} failed!")
            return False

    print("\n[SUCCESS] All tests passed! The bcrypt implementation is working correctly.")
    return True

if __name__ == "__main__":
    success = test_password_functions()
    if not success:
        print("\n[ERROR] Some tests failed!")
        sys.exit(1)
    else:
        print("\n[SUCCESS] All tests completed successfully!")