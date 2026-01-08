#!/usr/bin/env python3
"""
Main application entry point for the Console Task Manager.
Implements the main loop that allows user interaction.
"""
from src.models.task import Task
from src.repositories.task_repository import InMemoryTaskRepository
from src.views.cli_view import CLIView


class TaskController:
    """
    Main controller for user input processing.
    Coordinates between the view and repository layers.
    """
    def __init__(self):
        """Initialize the controller with repository and view."""
        self.repository = InMemoryTaskRepository()
        self.view = CLIView()

    def run(self):
        """Main application loop."""
        print("Welcome to Console Task Manager!")
        while True:
            self.view.display_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.toggle_task_status()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                print("\nGoodbye!")
                break
            else:
                self.view.display_error("Invalid choice. Please enter 1-6.")

    def add_task(self):
        """Handle adding a new task."""
        try:
            title, description = self.view.get_task_input()
            if not title:
                self.view.display_error("Task title cannot be empty.")
                return

            task = Task.create(title=title, description=description)
            self.repository.add(task)
            self.view.display_message(f"Task '{task.title}' added successfully with ID: {task.id}")
        except ValueError as e:
            self.view.display_error(str(e))
        except Exception as e:
            self.view.display_error(f"An error occurred while adding task: {str(e)}")

    def view_tasks(self):
        """Handle viewing all tasks."""
        try:
            tasks = self.repository.list_all()
            self.view.display_tasks(tasks)
        except Exception as e:
            self.view.display_error(f"An error occurred while viewing tasks: {str(e)}")

    def update_task(self):
        """Handle updating an existing task."""
        try:
            task_id = self.view.get_task_id()
            task = self.repository.get_by_id(task_id)
            if not task:
                self.view.display_error(f"Task with ID '{task_id}' not found.")
                return

            updates = self.view.get_task_update_input()
            if not updates:
                self.view.display_message("No updates provided.")
                return

            updated_task = self.repository.update(task_id, **updates)
            if updated_task:
                self.view.display_message(f"Task '{updated_task.title}' updated successfully.")
            else:
                self.view.display_error("Failed to update task.")
        except Exception as e:
            self.view.display_error(f"An error occurred while updating task: {str(e)}")

    def toggle_task_status(self):
        """Handle toggling a task's completion status."""
        try:
            task_id = self.view.get_task_id()
            task = self.repository.get_by_id(task_id)
            if not task:
                self.view.display_error(f"Task with ID '{task_id}' not found.")
                return

            updated_task = self.repository.toggle_status(task_id)
            if updated_task:
                status_str = "completed" if updated_task.status else "marked incomplete"
                self.view.display_message(f"Task '{updated_task.title}' {status_str}.")
            else:
                self.view.display_error("Failed to toggle task status.")
        except Exception as e:
            self.view.display_error(f"An error occurred while toggling task status: {str(e)}")

    def delete_task(self):
        """Handle deleting a task."""
        try:
            task_id = self.view.get_task_id()
            task = self.repository.get_by_id(task_id)
            if not task:
                self.view.display_error(f"Task with ID '{task_id}' not found.")
                return

            if self.view.confirm_action(f"delete task '{task.title}'"):
                deleted = self.repository.delete(task_id)
                if deleted:
                    self.view.display_message(f"Task '{task.title}' deleted successfully.")
                else:
                    self.view.display_error("Failed to delete task.")
            else:
                self.view.display_message("Delete operation cancelled.")
        except Exception as e:
            self.view.display_error(f"An error occurred while deleting task: {str(e)}")


def main():
    """Main entry point for the application."""
    controller = TaskController()
    controller.run()


if __name__ == "__main__":
    main()