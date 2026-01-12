"""
CLI View - Handles formatted data display for the console application.
"""
from typing import List
from src.models.task import Task


class CLIView:
    """
    CLI View for formatted data display.
    Provides methods for displaying tasks and user interface elements.
    """
    def __init__(self):
        """Initialize the CLI view."""
        pass

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "="*50)
        print("Console Task Manager")
        print("="*50)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Complete/Incomplete")
        print("5. Delete Task")
        print("6. Exit")
        print("-"*50)

    def get_user_choice(self) -> str:
        """
        Get user's menu choice.

        Returns:
            str: User's choice as a string
        """
        return input("Enter your choice (1-6): ").strip()

    def display_task(self, task: Task):
        """
        Display a single task with formatting.

        Args:
            task: The task to display
        """
        status_str = "X" if task.status else "O"
        print(f"[{status_str}] ID: {task.id}")
        print(f"    Title: {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print()

    def display_tasks(self, tasks: List[Task]):
        """
        Display a list of tasks with formatting.

        Args:
            tasks: List of tasks to display
        """
        if not tasks:
            print("\nNo tasks found.")
            return

        print(f"\nFound {len(tasks)} task(s):")
        print("-" * 50)
        for task in tasks:
            self.display_task(task)

    def get_task_input(self) -> tuple:
        """
        Get task details from user input.

        Returns:
            tuple: (title: str, description: str or None)
        """
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional, press Enter to skip): ").strip()
        description = description if description else None
        return title, description

    def get_task_id(self) -> str:
        """
        Get task ID from user input.

        Returns:
            str: Task ID entered by the user
        """
        return input("Enter task ID: ").strip()

    def get_task_update_input(self) -> dict:
        """
        Get task update details from user input.

        Returns:
            dict: Dictionary with optional title, description, status fields
        """
        updates = {}
        title = input("Enter new title (press Enter to skip): ").strip()
        if title:
            updates['title'] = title

        description = input("Enter new description (press Enter to skip): ").strip()
        if description:
            updates['description'] = description

        status_input = input("Enter new status (1 for complete, 0 for incomplete, press Enter to skip): ").strip()
        if status_input:
            updates['status'] = status_input.lower() in ['1', 'true', 'yes', 'y']

        return updates

    def display_message(self, message: str):
        """
        Display a message to the user.

        Args:
            message: Message to display
        """
        print(f"\n{message}")

    def display_error(self, error: str):
        """
        Display an error message to the user.

        Args:
            error: Error message to display
        """
        print(f"\n❌ Error: {error}")

    def confirm_action(self, action: str) -> bool:
        """
        Ask user to confirm an action.

        Args:
            action: The action to confirm

        Returns:
            bool: True if user confirms, False otherwise
        """
        confirm = input(f"Are you sure you want to {action}? (y/n): ").strip().lower()
        return confirm in ['y', 'yes']