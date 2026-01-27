---
id: "004"
title: "Add Task Editing Functionality"
stage: "red"
date: "2026-01-23"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "web-auth-todo"
branch: "001-web-auth-todo"
user: "Claude Sonnet 4.5"
command: "sp.implement"
labels: ["task-editing", "ui", "backend", "put-api"]
links:
  spec: "specs/001-web-auth-todo/spec.md"
  plan: "specs/001-web-auth-todo/plan.md"
  ticket: null
  adr: null
  pr: null
files:
  - "frontend/src/app/dashboard/page.tsx"
  - "backend/src/api/todos.py"
  - "specs/001-web-auth-todo/tasks.md"
tests:
  - "Manual testing of task editing functionality"
---

# Add Task Editing Functionality

## User Request
Add Task Editing functionality as per Phase II requirements.

In src/app/dashboard/page.tsx, add an 'Edit' button (pencil icon) to each task card.

When 'Edit' is clicked, the task title and description should become editable input fields.

Add a 'Save' and 'Cancel' button that appear during editing.

Implement a handleUpdate function to send a PUT request to /api/${user_id}/tasks/${task_id} with the updated data.

Update src/api/todos.py to include a @router.put endpoint that accepts the updated task data, validates the UUID, and updates the database record.

## Implementation Details

### Frontend Changes
1. **Added Pencil Icon Import** in `frontend/src/app/dashboard/page.tsx`:
   - Added `Pencil` from lucide-react to the imports

2. **Added State Variables** for managing editing:
   - `editingTask`: Tracks which task is currently being edited
   - `editTaskData`: Stores the temporary data for the task being edited

3. **Implemented Editing Functions**:
   - `startEditing()`: Sets the current task to editing mode and populates the edit fields
   - `cancelEditing()`: Cancels the editing and resets the state
   - `handleUpdate()`: Sends a PUT request to update the task data

4. **Updated Task Card UI**:
   - Added pencil icon button to initiate editing
   - Implemented conditional rendering for edit vs display mode
   - In edit mode: Shows input fields for title and description, priority selector, and save/cancel buttons
   - In display mode: Shows the original content with completion status

### Backend Changes
1. **Added PUT Endpoint** in `backend/src/api/todos.py`:
   - Created `@router.put("/{user_id}/tasks/{task_id}")` endpoint
   - Implemented proper UUID conversion and validation
   - Added authorization checks to ensure users can only update their own tasks
   - Added proper error handling for invalid UUIDs
   - Updated the updated_at timestamp when tasks are modified via PUT
   - Differentiated between PUT (full replacement) and PATCH (partial update) behaviors

### Task Tracking Updates
Updated the tasks.md file to reflect the completion of the task editing functionality.

## Files Modified

### frontend/src/app/dashboard/page.tsx
- Added Pencil icon import
- Added state variables for editing
- Implemented editing functions (startEditing, cancelEditing, handleUpdate)
- Updated task card UI to support edit/display modes

### backend/src/api/todos.py
- Added PUT endpoint for task updates
- Maintained existing PATCH endpoint for compatibility
- Added proper documentation for both endpoints

### specs/001-web-auth-todo/tasks.md
- Added tasks T039 and T040 to track the editing functionality implementation

## Testing
The functionality was manually tested by:
1. Creating tasks in the UI
2. Clicking the edit button on tasks
3. Modifying task titles, descriptions, and priorities
4. Saving changes and verifying they persist
5. Canceling edits and verifying changes are discarded
6. Confirming that the backend properly handles PUT requests and updates the database records

## Outcome
Successfully implemented the task editing functionality as requested. Users can now click the pencil icon on any task to edit its title, description, and priority. The UI provides save and cancel buttons during editing, and the backend properly handles the PUT requests to update task data. The implementation maintains proper security checks and UUID validation.