#!/usr/bin/env python3
"""
Test script to verify that the bcrypt implementation works correctly
in the context of the authentication system after switching from Passlib.
"""

import sys
import os

# Add the backend directory to the path so we can import the security module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'backend'))

from core.security import get_password_hash, verify_password

def test_password_functions_comprehensive():
    """Test the password hashing and verification functions comprehensively."""
    print("Testing password hashing and verification functions comprehensively...")

    # Test cases with various password types
    test_cases = [
        ("simple", "Simple password"),
        ("password123", "Common password"),
        ("This is a longer password with more characters!", "Longer password"),
        ("A" * 50, "Long password (50 chars)"),
        ("A" * 80, "Very long password (80 chars) - exceeds bcrypt 72-byte limit"),
        ("special!@#$%^&*()", "Password with special characters"),
        ("password with spaces", "Password with spaces"),
        ("123456789", "Numeric password"),
        ("", "Empty password"),
    ]

    for i, (password, description) in enumerate(test_cases):
        print(f"\nTest {i+1}: {description}")
        print(f"  Password length: {len(password.encode('utf-8'))} bytes")

        try:
            # Hash the password
            hashed = get_password_hash(password)
            print(f"  Hashed successfully: {hashed[:30]}...")

            # Verify the password
            is_valid = verify_password(password, hashed)
            print(f"  Verification: {'[PASS]' if is_valid else '[FAIL]'}")

            # Test with wrong password (only if the original password isn't empty)
            if password:
                wrong_verification = verify_password("wrong_password", hashed)
                print(f"  Wrong password verification: {'[PASS]' if not wrong_verification else '[FAIL]'}")
            else:
                print(f"  Skipped wrong password test (original password is empty)")

            # Final validation
            success = is_valid and (password == "" or not wrong_verification)
            if not success:
                print(f"  ERROR: Test {i+1} failed!")
                return False

        except Exception as e:
            print(f"  ERROR: Test {i+1} failed with exception: {e}")
            return False

    print("\n[SUCCESS] All comprehensive tests passed! The bcrypt implementation is working correctly.")
    return True

def test_hash_consistency():
    """Test that the same password produces different hashes but all verify correctly."""
    print("\nTesting hash consistency...")

    password = "consistent_test_password"

    # Generate multiple hashes for the same password
    hashes = [get_password_hash(password) for _ in range(5)]

    # Verify they're all different (due to random salt)
    unique_hashes = set(hashes)
    print(f"  Generated {len(hashes)} hashes, {len(unique_hashes)} unique (should be 5)")

    if len(unique_hashes) != 5:
        print("  ERROR: Hashes should be unique due to random salt!")
        return False

    # Verify all hashes work with the original password
    for i, hash_val in enumerate(hashes):
        if not verify_password(password, hash_val):
            print(f"  ERROR: Hash {i+1} doesn't verify with original password!")
            return False

    # Verify none of the hashes work with a wrong password
    for i, hash_val in enumerate(hashes):
        if verify_password("wrong_password", hash_val):
            print(f"  ERROR: Hash {i+1} incorrectly verifies with wrong password!")
            return False

    print("  [PASS] Hash consistency test passed!")
    return True

def test_edge_cases():
    """Test edge cases for password hashing."""
    print("\nTesting edge cases...")

    # Test with None (should fail gracefully or handle as string)
    try:
        # This should handle non-string input
        result = get_password_hash(None)
        # If it doesn't throw an error, verify it works
        is_valid = verify_password(None, result)
        print(f"  [PASS] Handled None input: verification = {is_valid}")
    except Exception as e:
        print(f"  [INFO] None input raised exception (expected): {e}")

    # Test with very long password that definitely exceeds 72 bytes
    very_long_password = "A" * 100  # 100 bytes, well over the 72-byte limit
    try:
        hashed = get_password_hash(very_long_password)
        is_valid = verify_password(very_long_password, hashed)
        print(f"  [PASS] Handled 100-byte password: verification = {is_valid}")

        if not is_valid:
            print("  ERROR: Very long password didn't verify correctly!")
            return False
    except Exception as e:
        print(f"  ERROR: Very long password failed: {e}")
        return False

    print("  [PASS] Edge cases test passed!")
    return True

def run_all_tests():
    """Run all tests."""
    print("Running comprehensive bcrypt implementation tests...\n")

    success = True
    success &= test_password_functions_comprehensive()
    success &= test_hash_consistency()
    success &= test_edge_cases()

    if success:
        print("\n[SUCCESS] All comprehensive tests completed successfully!")
        return True
    else:
        print("\n[ERROR] Some tests failed!")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    if not success:
        sys.exit(1)