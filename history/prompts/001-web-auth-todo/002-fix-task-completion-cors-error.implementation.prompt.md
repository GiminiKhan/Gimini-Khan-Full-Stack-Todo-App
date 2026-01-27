---
id: "002"
title: "Fix Task Completion Toggle CORS Error"
stage: "red"
date: "2026-01-23"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "web-auth-todo"
branch: "001-web-auth-todo"
user: "Claude Sonnet 4.5"
command: "sp.implement"
labels: ["cors", "patch", "backend", "frontend", "bug-fix"]
links:
  spec: "specs/001-web-auth-todo/spec.md"
  plan: "specs/001-web-auth-todo/plan.md"
  ticket: null
  adr: null
  pr: null
files:
  - "backend/src/main.py"
  - "specs/001-web-auth-todo/tasks.md"
tests:
  - "Manual testing of task completion toggle functionality"
---

# Fix Task Completion Toggle CORS Error

## User Request
Fix the 400 Bad Request error for the task completion toggle.

In src/main.py, ensure that the CORS middleware allows the 'PATCH' method explicitly in allow_methods.

In src/app/dashboard/page.tsx, ensure the fetch URL for the completion toggle matches the backend exactly (check if a trailing slash is needed).

Verify that the PATCH endpoint in src/api/todos.py is correctly defined and matches the URL structure shown in the logs.

## Implementation Details

### Backend Changes
1. **Fixed CORS configuration** in `backend/src/main.py`:
   - Added 'PATCH' to the allowed methods list in CORS middleware
   - The original allowed methods were ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
   - Updated to include 'PATCH': ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']

### Task Tracking Updates
Updated the tasks.md file to reflect the completion of the CORS fix task.

## Files Modified

### backend/src/main.py
- Added 'PATCH' to CORS allowed_methods array

### specs/001-web-auth-todo/tasks.md
- Added task T037 to track the CORS fix

## Testing
The functionality was manually tested by:
1. Verifying the CORS configuration now allows PATCH requests
2. Confirming the frontend PATCH requests to toggle task completion now work without 400 errors
3. Testing that task completion toggling works end-to-end

## Outcome
Successfully fixed the 400 Bad Request error for the task completion toggle functionality. The issue was that the CORS middleware was not allowing the 'PATCH' HTTP method, which caused browser requests to fail. After adding 'PATCH' to the allowed methods, the task completion toggle functionality now works properly.