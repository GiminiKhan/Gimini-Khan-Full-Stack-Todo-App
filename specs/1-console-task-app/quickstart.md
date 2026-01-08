# Quickstart Guide: Console Task App

**Feature**: Console Task App
**Date**: 2025-12-30

## Getting Started

### Prerequisites
- Python 3.13+
- uv package manager

### Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies using uv:
   ```bash
   uv sync
   ```
4. Run the application:
   ```bash
   uv run main.py
   ```

### Usage
Once the application starts, you'll see a menu with the following options:
1. Add Task - Create a new task with title and description
2. View Tasks - See all tasks with their status indicators
3. Update Task - Modify an existing task's details
4. Mark Complete - Toggle a task's completion status
5. Delete Task - Remove a task by ID
6. Exit - Quit the application

### Example Workflow
1. Launch the app: `uv run main.py`
2. Select "1" to add a task
3. Enter a title and description
4. Select "2" to view all tasks
5. Select "4" to mark a task as complete/incomplete
6. Select "6" to exit

## Development
To run tests:
```bash
uv run pytest
```

To run the application in development mode:
```bash
uv run main.py
```
