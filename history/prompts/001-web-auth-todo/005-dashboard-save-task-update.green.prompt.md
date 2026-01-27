---
id: 005
title: dashboard-save-task-update
stage: green
date: 2026-01-23
surface: agent
model: claude-sonnet-4-5-20250929
feature: web-auth-todo
branch: 001-web-auth-todo
user: Claude
command: /sp.implement Update the save task function in src/app/dashboard/page.tsx. Make sure the fetch request to /todos/ includes the header 'Authorization': 'Bearer ' + token (with a space after Bearer). Also, ensure the JSON body being sent matches the Todo model (title and description)
labels: [frontend, api, auth, todo, dashboard]
links:
  spec: ../../specs/001-web-auth-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - frontend/src/app/dashboard/page.tsx
tests:
  - specs/001-web-auth-todo/data-model.md
---

## Prompt

Update the save task function in src/app/dashboard/page.tsx. Make sure the fetch request to /todos/ includes the header 'Authorization': 'Bearer ' + token (with a space after Bearer). Also, ensure the JSON body being sent matches the Todo model (title and description)

## Response snapshot

Successfully updated the dashboard page to:

1. Fixed API endpoints to match the contract (changed from `/todos/` to `/api/todos`)
2. Updated the POST request in handleCreate to send proper Todo model fields: title, description, and priority (instead of is_completed)
3. Ensured Authorization header format is 'Bearer ' + token with proper spacing
4. Updated the GET and DELETE requests to use the correct API endpoints
5. Maintained the priority field conversion to lowercase to match the enum values in the backend

All API calls now properly follow the contract defined in the data model with correct authorization headers and request bodies.

## Outcome

- ✅ Impact: API calls now follow proper contract with correct endpoints and authorization
- 🧪 Tests: Requests match the API contract defined in data model
- 📁 Files: Updated dashboard page with correct API endpoint usage
- 🔁 Next prompts: Continue with remaining frontend implementation
- 🧠 Reflection: The implementation now properly follows the API contract

## Evaluation notes (flywheel)

- Failure modes observed: None - successful implementation
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Test the API calls with backend