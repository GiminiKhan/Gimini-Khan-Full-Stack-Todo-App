---
id: "003"
title: "Fix UUID Conversion Error in Task API Functions"
stage: "red"
date: "2026-01-23"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "web-auth-todo"
branch: "001-web-auth-todo"
user: "Claude Sonnet 4.5"
command: "sp.implement"
labels: ["uuid", "database", "backend", "bug-fix"]
links:
  spec: "specs/001-web-auth-todo/spec.md"
  plan: "specs/001-web-auth-todo/plan.md"
  ticket: null
  adr: null
  pr: null
files:
  - "backend/src/api/todos.py"
  - "specs/001-web-auth-todo/tasks.md"
tests:
  - "Manual testing of task CRUD operations with UUID parameters"
---

# Fix UUID Conversion Error in Task API Functions

## User Request
Fix the UUID conversion error in src/api/todos.py for the toggle_task_completion function. Inside the function, ensure that the task_id (which is coming as a string from the URL) is converted to a UUID object using uuid.UUID(task_id) before it is used in the database query db.exec(statement).first(). This will resolve the 'str object has no attribute hex' error.

## Implementation Details

### Backend Changes
1. **Added uuid import** to `backend/src/api/todos.py`:
   - Added `import uuid` to the imports section

2. **Fixed UUID conversion** in multiple API functions:
   - Fixed `toggle_task_completion` function to convert string task_id to UUID object
   - Added proper error handling for invalid UUID strings
   - Fixed `get_task` function with the same UUID conversion logic
   - Fixed `update_task` function with the same UUID conversion logic
   - Fixed `delete_task` function with the same UUID conversion logic

### Task Tracking Updates
Updated the tasks.md file to reflect the completion of the UUID fix task.

## Files Modified

### backend/src/api/todos.py
- Added uuid import
- Added UUID conversion logic to all functions that query by task ID
- Added proper exception handling for invalid UUID strings

### specs/001-web-auth-todo/tasks.md
- Added task T038 to track the UUID conversion fix

## Testing
The functionality was manually tested by:
1. Verifying that all task CRUD operations work properly with UUID parameters
2. Testing that invalid UUID strings return proper error responses
3. Confirming that the original 'str object has no attribute hex' error is resolved

## Outcome
Successfully fixed the UUID conversion error in the task API functions. The issue was that the Todo model uses UUID as the primary key, but the API functions were comparing string task_id parameters directly to UUID database columns. Now all functions properly convert string task_id parameters to UUID objects before database queries, resolving the 'str object has no attribute hex' error.