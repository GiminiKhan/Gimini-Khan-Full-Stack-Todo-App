# Data Model: Console Task App

**Feature**: Console Task App
**Date**: 2025-12-30

## Entities

### Task
Represents a single task with properties for management and tracking.

**Fields**:
- `id`: UUID string (unique identifier, generated automatically)
- `title`: String (task title, required)
- `description`: String (task description, optional)
- `status`: Boolean (task completion status, default: False for incomplete)

**Validation Rules**:
- `title` must not be empty or contain only whitespace
- `id` must be unique within the system
- `status` is boolean (True = complete, False = incomplete)

**State Transitions**:
- `incomplete` (status=False) → `complete` (status=True) when marked complete
- `complete` (status=True) → `incomplete` (status=False) when marked incomplete

**Relationships**:
- None (standalone entity)

## Data Flow

### Creation
1. User provides title and description
2. System generates unique UUID for the task
3. Status is set to False (incomplete) by default
4. Task is stored in the in-memory repository

### Reading
1. Tasks can be retrieved individually by ID
2. All tasks can be retrieved as a list
3. Tasks are returned with all their properties

### Updating
1. User provides task ID and new title/description values
2. System validates the new values
3. Task properties are updated in the repository

### Deletion
1. User provides task ID
2. System removes the task from the repository
3. Task is no longer accessible

## Storage Structure

The in-memory storage uses a Python dictionary with the following structure:
```python
{
    "task_id_1": Task(id="task_id_1", title="Task 1", description="Description", status=False),
    "task_id_2": Task(id="task_id_2", title="Task 2", description="Description", status=True),
    ...
}
```

This structure allows for O(1) lookup by task ID and efficient CRUD operations.