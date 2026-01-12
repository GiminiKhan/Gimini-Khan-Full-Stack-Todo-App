# Console Task Manager

A simple console-based task management application built with Python. This application allows users to manage tasks through a command-line interface with full CRUD (Create, Read, Update, Delete) functionality.

## Features

- Add new tasks with title and description
- View all tasks with status indicators
- Update existing task details
- Mark tasks as complete/incomplete
- Delete tasks by ID
- In-memory storage (no database required)

## Requirements

- Python 3.13+
- `uv` package manager (optional, for virtual environment management)

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies (if any are added later):
   ```bash
   uv sync  # or pip install -r requirements.txt if available
   ```

## Usage

Run the application:
```bash
python main.py
```

The application will present a menu with the following options:
1. Add Task - Create a new task with title and description
2. View Tasks - See all tasks with their status indicators
3. Update Task - Modify an existing task's details
4. Mark Complete/Incomplete - Toggle a task's completion status
5. Delete Task - Remove a task by ID
6. Exit - Quit the application

## Architecture

The application follows Clean Architecture principles with the following layers:

- **Models**: Task model with validation
- **Repositories**: In-memory task repository with CRUD operations
- **Controllers**: Task controller for business logic
- **Views**: CLI view for user interface

## Project Structure

```
src/
├── models/
│   └── task.py          # Task model
├── repositories/
│   └── task_repository.py  # In-memory repository
├── controllers/
│   └── task_controller.py  # (Integrated in main.py)
└── views/
    └── cli_view.py      # CLI interface
main.py                  # Main application entry point
pyproject.toml           # Project configuration
```

## Development

To run tests:
```bash
python test_app.py
```

## License

This project is open source and available under the MIT License.