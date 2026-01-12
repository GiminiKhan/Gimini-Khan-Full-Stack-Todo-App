---
id: 001
title: Todo and Project CRUD Implementation
stage: tasks
date: 2026-01-06
surface: agent
model: Claude Sonnet 4.5
feature: phase2-web
branch: main
user: Claude Code
command: sp.implement
labels: ["todo", "project", "crud", "api", "backend"]
links:
  spec: specs/phase2-web/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - src/backend/api/deps.py
 - src/backend/api/schemas/todo.py
 - src/backend/api/schemas/project.py
 - src/backend/api/routes/projects.py
 - src/backend/api/routes/todos.py
 - src/backend/main.py
 - specs/phase2-web/tasks.md
tests:
 - null
---

## Prompt

Task T-005: Todo and Project CRUD Implementation

# Role: Master Architect
# Context: Auth is ready. Now implementing core features.

Please follow these steps:

1. **Dependencies**: `src/backend/api/deps.py` banayein jo `get_current_user` ki dependency handle kare (JWT token verify karke user object return kare).
2. **Schemas**:
   - `src/backend/api/schemas/todo.py` (TodoCreate, TodoUpdate, TodoResponse).
   - `src/backend/api/schemas/project.py` (ProjectCreate, ProjectUpdate, ProjectResponse).
3. **API Routes**:
   - `src/backend/api/routes/projects.py`: Full CRUD (Get all, Get by ID, Create, Update, Delete). Ensure only owner can access.
   - `src/backend/api/routes/todos.py`: Full CRUD. Add filter to get todos by project_id.
4. **Integration**: In routes ko `src/backend/main.py` mein include karein `/api/v1/projects` aur `/api/v1/todos` ke under.
5. **PHR**: Is progress ka record `history/prompts/phase2-web/` mein save karein.

Note: Har API endpoint ko `get_current_user` se protect karein taake unautho

## Response snapshot

Successfully implemented the Todo and Project CRUD functionality:

1. Created `src/backend/api/deps.py` with `get_current_user` dependency that validates JWT tokens and returns the authenticated user
2. Created `src/backend/api/schemas/todo.py` with TodoCreate, TodoUpdate, and TodoResponse schemas
3. Created `src/backend/api/schemas/project.py` with ProjectCreate, ProjectUpdate, and ProjectResponse schemas
4. Created `src/backend/api/routes/projects.py` with full CRUD operations (GET all, GET by ID, POST, PUT, DELETE) with proper authentication and authorization checks
5. Created `src/backend/api/routes/todos.py` with full CRUD operations and additional features:
   - GET all todos with filtering by project_id, completion status, and priority
   - GET by ID
   - POST to create new todos
   - PUT to update todos
   - PATCH to update completion status
   - DELETE to remove todos
6. Updated `src/backend/main.py` to include the new routes under `/api/v1/` prefix
7. Updated `specs/phase2-web/tasks.md` to track the completed tasks

All endpoints are protected with the `get_current_user` dependency to ensure only authenticated users can access their own data. The implementation follows the architecture plan and includes proper error handling and validation.

## Outcome

- ✅ Impact: Core CRUD functionality for Todo and Project entities implemented with authentication
- 🧪 Tests: null
- 📁 Files: 7 files modified/created to implement the full CRUD functionality
- 🔁 Next prompts: Testing and frontend integration
- 🧠 Reflection: Implementation followed the planned architecture with proper security measures

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null