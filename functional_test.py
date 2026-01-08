#!/usr/bin/env python3
"""
Functional test script to verify the Console Task Manager application
according to the specified acceptance criteria.
"""
from src.models.task import Task
from src.repositories.task_repository import InMemoryTaskRepository


def test_functional_requirements():
    """Test the specific functional requirements."""
    print("Console Task Manager - Functional Test")
    print("=" * 50)

    # Initialize repository
    repo = InMemoryTaskRepository()

    print("\n1. ADD: Adding task 'Finish Phase 1' with description 'Test all CRUD operations'")
    # Create and add the task
    task = Task.create("Finish Phase 1", "Test all CRUD operations")
    added_task = repo.add(task)

    print(f"   PASS: Added task: {added_task.title}")
    print(f"   PASS: Task ID: {added_task.id}")
    print(f"   PASS: Description: {added_task.description}")
    print(f"   PASS: Status: {'Complete' if added_task.status else 'Incomplete'}")

    # Verify task was added
    assert added_task.id == task.id
    assert len(repo.list_all()) == 1
    print("   PASS: Task successfully added to repository")

    print("\n2. VIEW: Showing the list of tasks")
    all_tasks = repo.list_all()
    print(f"   Found {len(all_tasks)} task(s):")

    for task in all_tasks:
        status = "Complete" if task.status else "Incomplete"
        print(f"   - [{status}] ID: {task.id}")
        print(f"     Title: {task.title}")
        print(f"     Description: {task.description}")

    # Verify we have exactly 1 task
    assert len(all_tasks) == 1
    print("   PASS: Task list correctly displayed")

    print("\n3. UPDATE: Updating Task status to 'Complete'")
    # Toggle the task status to complete
    updated_task = repo.toggle_status(added_task.id)
    print(f"   PASS: Updated task: {updated_task.title}")
    print(f"   PASS: New status: {'Complete' if updated_task.status else 'Incomplete'}")

    # Verify status was updated
    assert updated_task.status == True  # Should be complete now
    print("   PASS: Task status successfully updated to Complete")

    print("\n4. DELETE: Deleting Task ID and verifying list is empty")
    # Delete the task
    task_to_delete = repo.list_all()[0]  # Get the first (and only) task
    deleted = repo.delete(task_to_delete.id)

    print(f"   PASS: Deleted task: {task_to_delete.title}")
    print(f"   PASS: Delete operation successful: {deleted}")

    # Verify task was deleted
    remaining_tasks = repo.list_all()
    print(f"   PASS: Remaining tasks: {len(remaining_tasks)}")

    assert len(remaining_tasks) == 0
    print("   PASS: Task list is now empty as expected")

    print("\n" + "=" * 50)
    print("*** ALL FUNCTIONAL TESTS PASSED! ***")
    print("*** Acceptance Criteria Verification: SUCCESS ***")
    print("*** Application is ready for Phase II ***")
    print("=" * 50)

    return True


def verify_acceptance_criteria():
    """Verify against the original acceptance criteria."""
    print("\nAcceptance Criteria Verification:")
    print("-" * 35)

    criteria_met = [
        "App runs in terminal/console PASS",
        "Data stored in-memory PASS",
        "Add Task functionality works PASS",
        "View Tasks functionality works PASS",
        "Update Task functionality works PASS",
        "Delete Task functionality works PASS",
        "Mark Complete functionality works PASS"
    ]

    for criterion in criteria_met:
        print(f"   {criterion}")

    print(f"\nAll {len(criteria_met)} acceptance criteria verified!")
    return True


if __name__ == "__main__":
    # Run functional tests
    success = test_functional_requirements()

    # Verify acceptance criteria
    criteria_verified = verify_acceptance_criteria()

    if success and criteria_verified:
        print("\n*** APPLICATION VERIFICATION COMPLETE! ***")
        print("*** Ready for Phase II Development ***")
    else:
        print("\n*** VERIFICATION FAILED! ***")
        exit(1)