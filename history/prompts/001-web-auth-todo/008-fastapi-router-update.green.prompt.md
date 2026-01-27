---
id: 008
title: fastapi-router-update
stage: green
date: 2026-01-23
surface: agent
model: claude-sonnet-4-5-20250929
feature: web-auth-todo
branch: 001-web-auth-todo
user: Claude
command: /sp.implement Update the FastAPI router in src/api/todos.py (or tasks.py) to match Phase II requirements. Change the prefix to /api and update the route paths to include {user_id}/tasks. Ensure that the user_id in the URL is validated against the authenticated user's ID from the JWT token
labels: [backend, api, auth, router, endpoint]
links:
  spec: ../../specs/001-web-auth-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - backend/src/api/todos.py
tests:
  -

---

## Prompt

Update the FastAPI router in src/api/todos.py (or tasks.py) to match Phase II requirements. Change the prefix to /api and update the route paths to include {user_id}/tasks. Ensure that the user_id in the URL is validated against the authenticated user's ID from the JWT token

## Response snapshot

Successfully updated the FastAPI router to match Phase II requirements:

1. Changed the router prefix from `/todos` to `/api`
2. Updated all route paths to include `{user_id}/tasks` pattern:
   - GET /{user_id}/tasks (was GET /)
   - POST /{user_id}/tasks (was POST /)
   - GET /{user_id}/tasks/{task_id} (was GET /{todo_id})
   - PATCH /{user_id}/tasks/{task_id} (was PATCH /{todo_id})
   - DELETE /{user_id}/tasks/{task_id} (was DELETE /{todo_id})
3. Added validation to ensure the user_id in the URL matches the authenticated user's ID from the JWT token
4. Renamed functions from 'todo' to 'task' terminology for consistency
5. Updated function parameters to accept user_id and validate against current_user

All endpoints now properly follow the new API pattern with user validation.

## Outcome

- ✅ Impact: API endpoints now follow Phase II requirements with user validation
- 🧪 Tests: All endpoints validate user_id against authenticated user
- 📁 Files: Updated todos.py with new endpoint pattern
- 🔁 Next prompts: Test the new endpoints
- 🧠 Reflection: The implementation ensures proper user isolation and validation

## Evaluation notes (flywheel)

- Failure modes observed: None - successful implementation
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Test API with frontend integration