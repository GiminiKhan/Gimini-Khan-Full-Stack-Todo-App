#!/usr/bin/env python3
"""
Simple test script to verify the Console Task App functionality.
"""
from src.models.task import Task
from src.repositories.task_repository import InMemoryTaskRepository
from src.views.cli_view import CLIView


def test_task_creation():
    """Test task creation functionality."""
    print("Testing Task Creation...")

    # Create a task
    task = Task.create("Test Task", "This is a test task")

    # Verify task properties
    assert task.title == "Test Task"
    assert task.description == "This is a test task"
    assert task.status == False  # Should be incomplete by default
    assert task.id is not None
    assert len(task.id) > 0

    print("PASS: Task creation test passed")


def test_repository_crud():
    """Test repository CRUD operations."""
    print("\nTesting Repository CRUD Operations...")

    repo = InMemoryTaskRepository()

    # Create and add a task
    task = Task.create("Test Task", "Description")
    added_task = repo.add(task)

    assert added_task.id == task.id
    assert len(repo.list_all()) == 1

    # Retrieve the task
    retrieved_task = repo.get_by_id(task.id)
    assert retrieved_task is not None
    assert retrieved_task.title == "Test Task"

    # Update the task
    updated_task = repo.update(task.id, title="Updated Task")
    assert updated_task is not None
    assert updated_task.title == "Updated Task"

    # Toggle status
    toggled_task = repo.toggle_status(task.id)
    assert toggled_task is not None
    assert toggled_task.status == True  # Should be complete after toggle

    # Delete the task
    deleted = repo.delete(task.id)
    assert deleted == True
    assert len(repo.list_all()) == 0

    print("PASS: Repository CRUD test passed")


def test_task_validation():
    """Test task validation."""
    print("\nTesting Task Validation...")

    try:
        # This should raise a ValueError
        invalid_task = Task.create("")
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        print("PASS: Task validation test passed")


def run_all_tests():
    """Run all tests."""
    print("Running Console Task App Tests...\n")

    test_task_creation()
    test_repository_crud()
    test_task_validation()

    print("\n*** All tests passed! ***")


if __name__ == "__main__":
    run_all_tests()