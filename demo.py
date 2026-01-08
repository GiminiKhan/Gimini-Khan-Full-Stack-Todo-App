#!/usr/bin/env python3
"""
Demo script to show the Console Task Manager functionality.
"""
from src.models.task import Task
from src.repositories.task_repository import InMemoryTaskRepository
from src.views.cli_view import CLIView


def demo_functionality():
    """Demonstrate the core functionality of the task manager."""
    print("Console Task Manager - Functionality Demo")
    print("=" * 50)

    # Initialize repository and view
    repo = InMemoryTaskRepository()
    view = CLIView()

    print("\n1. Creating tasks...")
    # Create some sample tasks
    task1 = Task.create("Buy groceries", "Milk, bread, eggs")
    task2 = Task.create("Finish project", "Complete the console app implementation")
    task3 = Task.create("Call mom", "Check on her health")

    # Add tasks to repository
    repo.add(task1)
    repo.add(task2)
    repo.add(task3)

    print(f"   Created task: {task1.title}")
    print(f"   Created task: {task2.title}")
    print(f"   Created task: {task3.title}")

    print("\n2. Viewing all tasks...")
    all_tasks = repo.list_all()
    view.display_tasks(all_tasks)

    print("\n3. Updating a task...")
    # Update task2
    updated_task = repo.update(task2.id, title="Finish project today",
                              description="Complete the console app implementation by EOD")
    print(f"   Updated task: {updated_task.title}")

    print("\n4. Marking a task as complete...")
    # Mark task1 as complete
    completed_task = repo.toggle_status(task1.id)
    print(f"   Completed task: {completed_task.title} (Status: {'Complete' if completed_task.status else 'Incomplete'})")

    print("\n5. Viewing tasks after updates...")
    all_tasks = repo.list_all()
    view.display_tasks(all_tasks)

    print("\n6. Deleting a task...")
    # Delete task3
    deleted = repo.delete(task3.id)
    print(f"   Deleted task: {task3.title} (Success: {deleted})")

    print("\n7. Final task list...")
    final_tasks = repo.list_all()
    view.display_tasks(final_tasks)

    print("\nDemo completed successfully!")


if __name__ == "__main__":
    demo_functionality()