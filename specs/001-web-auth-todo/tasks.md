---
description: "Task list template for feature implementation"
---

# Tasks: Web Authentication and Todo Management

**Input**: Design documents from `/specs/001-web-auth-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/
**Constitution Compliance**: All tasks must adhere to constitution principles (Spec-Driven Development, No Manual Code, Agentic Stack, Clean Architecture, Process Integrity, Security Protocol, Frontend Standard, UI/UX Standards)

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in backend/ and frontend/
- [ ] T002 [P] Initialize Python project with FastAPI dependencies in backend/
- [ ] T003 [P] Initialize Next.js 15+ project with TypeScript in frontend/
- [ ] T004 [P] Configure Tailwind CSS with Indigo & Slate theme in frontend/
- [ ] T005 [P] Configure Better Auth integration in frontend/
- [ ] T006 Setup environment configuration management for both backend and frontend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T007 Setup Neon PostgreSQL database schema and migrations framework in backend/
- [X] T008 [P] Configure Better Auth middleware in FastAPI backend/
- [X] T009 [P] Setup database connection pool in backend/src/core/database.py
- [X] T010 Create base User and Todo models in backend/src/models/ using SQLModel
- [X] T011 Configure error handling and logging infrastructure in backend/
- [X] T012 Setup CORS and security middleware in backend/
- [X] T013 Create API client service in frontend/src/services/api-client.ts

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure Login and Todo Dashboard Access (Priority: P1) 🎯 MVP

**Goal**: Implement authentication flow that redirects unauthenticated users to /auth/login and protects the /dashboard route

**Independent Test**: Can be fully tested by navigating to the root URL and verifying redirect to /auth/login, then completing login flow and accessing /dashboard with user-specific data.

### Implementation for User Story 1

- [X] T014 [P] [US1] Create User model in backend/src/models/user.py with SQLModel
- [X] T015 [P] [US1] Create Todo model in backend/src/models/todo.py with SQLModel
- [X] T016 [US1] Implement authentication service in backend/src/services/auth_service.py
- [X] T016.1 [P] [US1] Update auth_service.py to import security utilities from backend/src/core/security.py
- [X] T016.2 [P] [US1] Replace fake-token logic with JWT generation in authenticate_user method
- [X] T016.3 [P] [US1] Verify backend correctly returns encrypted JWT token with proper token_type
- [ ] T017 [US1] Implement auth endpoints in backend/src/api/auth.py
- [X] T018 [US1] Create login page component in frontend/src/app/auth/login/page.tsx
- [X] T019 [US1] Create dashboard page component in frontend/src/app/dashboard/page.tsx
- [X] T020 [US1] Implement Auth Guard component in frontend/src/components/ui/auth-guard.tsx
- [X] T021 [US1] Implement Protected Layout in frontend/src/components/layouts/protected-layout.tsx
- [ ] T022 [US1] Configure route protection middleware for /dashboard in Next.js
- [ ] T023 [US1] Add redirect logic to /auth/login for unauthenticated users

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Todo Management Operations (Priority: P2)

**Goal**: Enable authenticated users to perform CRUD operations on their todo items, including creating, viewing, updating, and deleting tasks with proper priority indicators.

**Independent Test**: Can be fully tested by authenticating as a user and performing all CRUD operations on todo items with different priority levels.

### Implementation for User Story 2

- [X] T024 [P] [US2] Implement Todo service in backend/src/services/todo_service.py
- [X] T025 [P] [US2] Create todos API endpoints in backend/src/api/todos.py
- [X] T026 [P] [US2] Add dependency injection for auth in backend/src/api/deps.py
- [X] T027 [US2] Implement Todo client service in frontend/src/services/todo-client.ts
- [X] T028 [US2] Create Todo form component in frontend/src/components/forms/todo-form.tsx
- [X] T029 [US2] Create Todo card component in frontend/src/components/ui/todo-card.tsx
- [X] T030 [US2] Implement Todo CRUD operations in dashboard page
- [X] T031 [US2] Add axios interceptors for Authorization header in frontend/src/services/api-client.ts
- [X] T032 [US2] Map API endpoints to /api/todos in frontend services
- [X] T033 [US2] Implement error handling for API calls
- [X] T035 [US2] Add task completion toggle functionality in frontend/src/app/dashboard/page.tsx
- [X] T036 [US2] Add PATCH endpoint for toggling task completion in backend/src/api/todos.py
- [X] T037 [US2] Fix CORS to allow PATCH method in backend/src/main.py
- [X] T038 [US2] Fix UUID conversion error in toggle_task_completion function in backend/src/api/todos.py
- [X] T039 [US2] Add task editing functionality in frontend/src/app/dashboard/page.tsx
- [X] T040 [US2] Add PUT endpoint for task updates in backend/src/api/todos.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Enhanced UI Experience (Priority: P3)

**Goal**: Implement modern, visually appealing interface with consistent styling, smooth loading states, and intuitive priority indicators.

**Independent Test**: Can be fully tested by evaluating the visual presentation, loading states, and consistency of UI elements across all pages.

### Implementation for User Story 3

- [X] T034 [P] [US3] Create Skeleton loader component in frontend/src/components/ui/skeleton-loader.tsx
- [X] T035 [P] [US3] Update Todo card with rounded-2xl corners and soft shadows
- [X] T036 [US3] Implement glassmorphism effect for Todo cards
- [X] T037 [US3] Add priority indicator styling with color-coded badges (High: Red, Medium: Amber, Low: Blue)
- [X] T038 [US3] Replace basic loading indicators with professional Tailwind Skeleton loaders
- [X] T039 [US3] Implement Indigo & Slate theme throughout the application
- [X] T040 [US3] Add Sidebar navigation component
- [X] T041 [US3] Update global styles in frontend/src/styles/globals.css
- [X] T042 [US3] Ensure responsive design across all components
- [X] T043 [US3] Implement accessibility features for all UI components

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T044 [P] Update documentation in docs/
- [ ] T045 Code cleanup and refactoring across all components
- [ ] T046 Performance optimization across all stories
- [ ] T047 [P] Additional unit tests in backend/tests/ and frontend/tests/
- [ ] T048 Security hardening for all endpoints
- [ ] T049 Run quickstart.md validation to ensure all features work correctly
- [ ] T050 Final integration testing of all user stories together

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 authentication but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Depends on US1/US2 components but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Create User model in backend/src/models/user.py"
Task: "Create Todo model in backend/src/models/todo.py"

# Launch all components for User Story 1 together:
Task: "Create login page component in frontend/src/app/auth/login/page.tsx"
Task: "Create dashboard page component in frontend/src/app/dashboard/page.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence