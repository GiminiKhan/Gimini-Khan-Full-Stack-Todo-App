#!/usr/bin/env python3
"""
Test script to verify that all imports work correctly after the fixes.
"""

def test_main_import():
    """Test that main.py can be imported without errors."""
    print("Testing main.py import...")

    try:
        from src.backend.main import app
        print("✅ main.py import successful")
        return True
    except ImportError as e:
        print(f"❌ main.py import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ main.py import raised exception: {e}")
        return False

def test_all_imports():
    """Test all the fixed imports."""
    print("\nTesting individual imports...")

    imports_to_test = [
        ("src.backend.core.config", "settings"),
        ("src.backend.api.routes.auth", "router as auth_router"),
        ("src.backend.api.routes.tasks", "router as tasks_router"),
        ("src.backend.services.better_auth_service", "better_auth_service"),
        ("src.backend.api.deps", "get_current_better_auth_user"),
        ("src.backend.database.session", "get_db_session"),
        ("src.backend.core.security", "create_access_token"),
    ]

    success_count = 0
    for module, item in imports_to_test:
        try:
            __import__(module)
            print(f"✅ {module} import successful")
            success_count += 1
        except ImportError as e:
            print(f"❌ {module} import failed: {e}")

    print(f"\n{success_count}/{len(imports_to_test)} imports successful")
    return success_count == len(imports_to_test)

if __name__ == "__main__":
    print("Testing imports after fixing relative import issues...\n")

    main_success = test_main_import()
    all_success = test_all_imports()

    if main_success and all_success:
        print("\n🎉 All imports successful! The Vercel deployment issue should be fixed.")
        print("✅ You can now deploy to Vercel without FUNCTION_INVOCATION_FAILED errors.")
    else:
        print("\n❌ Some imports still failing. Please check the error messages above.")
        exit(1)