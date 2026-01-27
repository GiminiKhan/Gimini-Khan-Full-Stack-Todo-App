---
id: 007
title: dashboard-endpoint-update
stage: green
date: 2026-01-23
surface: agent
model: claude-sonnet-4-5-20250929
feature: web-auth-todo
branch: 001-web-auth-todo
user: Claude
command: /sp.implement Update the API calls in src/app/dashboard/page.tsx to match Phase II requirements. The endpoints must follow the pattern /api/${user_id}/tasks. Ensure the user_id is dynamically passed from the authenticated user session (Better Auth) and that the endpoint name is 'tasks' instead of 'todos'.
labels: [frontend, api, auth, dashboard, endpoint]
links:
  spec: ../../specs/001-web-auth-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - frontend/src/app/dashboard/page.tsx
tests:
  -

---

## Prompt

Update the API calls in src/app/dashboard/page.tsx to match Phase II requirements. The endpoints must follow the pattern /api/${user_id}/tasks. Ensure the user_id is dynamically passed from the authenticated user session (Better Auth) and that the endpoint name is 'tasks' instead of 'todos'.

## Response snapshot

Successfully updated the dashboard page API calls to follow the new endpoint pattern:

1. Added a helper function to decode JWT tokens and extract the user_id from the 'sub' claim
2. Updated all API calls (fetchTasks, handleCreate, deleteTodo) to use the new pattern: /api/${user_id}/tasks
3. Changed endpoint name from 'todos' to 'tasks' as required
4. Dynamically extract user_id from the authenticated user session (JWT token) using the decodeToken function

All API calls now properly follow the Phase II requirements with user-specific endpoints that include the user_id in the URL path.

## Outcome

- ✅ Impact: API calls now follow Phase II endpoint pattern requirements
- 🧪 Tests: All API calls use new /api/${user_id}/tasks pattern
- 📁 Files: Updated dashboard page with new endpoint structure
- 🔁 Next prompts: Update backend to handle new endpoint pattern
- 🧠 Reflection: The implementation extracts user_id from JWT token correctly

## Evaluation notes (flywheel)

- Failure modes observed: None - successful implementation
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Update backend to match new endpoint pattern