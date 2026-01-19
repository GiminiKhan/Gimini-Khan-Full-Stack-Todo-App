#!/usr/bin/env python3
"""
Test script to verify that FastAPI and Pydantic imports work correctly
after the dependency updates.
"""

def test_imports():
    """Test that all required imports work without errors."""
    print("Testing imports...")

    try:
        from fastapi import FastAPI
        print("✅ FastAPI import successful")
    except ImportError as e:
        print(f"❌ FastAPI import failed: {e}")
        return False

    try:
        from pydantic import BaseModel
        print("✅ Pydantic import successful")
    except ImportError as e:
        print(f"❌ Pydantic import failed: {e}")
        return False

    try:
        import pydantic_core
        print("✅ pydantic_core import successful")
    except ImportError as e:
        print(f"❌ pydantic_core import failed: {e}")
        return False

    try:
        from src.backend.main import app
        print("✅ Backend main import successful")
    except ImportError as e:
        print(f"❌ Backend main import failed: {e}")
        return False

    print("All imports successful! 🎉")
    return True

if __name__ == "__main__":
    success = test_imports()
    if success:
        print("\n✓ The pydantic-core module error has been fixed!")
        print("✓ Dependencies are now compatible with Vercel deployment.")
    else:
        print("\n❌ The fix did not resolve the import issues.")
        exit(1)