---
description: "Task list template for feature implementation"
---

# Tasks: Console Task App

**Input**: Design documents from `/specs/1-console-task-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/
**Constitution Compliance**: All tasks must adhere to constitution principles (Spec-Driven Development, No Manual Code, Agentic Stack, Clean Architecture, Process Integrity)

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

- [x] T001 [P] Create project structure per implementation plan in src/
- [x] T002 [P] Initialize Python project with uv and create pyproject.toml
- [x] T003 [P] Configure linting and formatting tools (ruff, black, mypy)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task model with required fields (ID, title, description, status) in src/models/task.py
- [x] T005 [P] Implement InMemory Repository with CRUD methods in src/repositories/task_repository.py
- [x] T006 Setup CLI interface structure using cmd module in src/views/cli_view.py
- [x] T007 Create main application entry point in main.py
- [x] T008 [P] Setup basic testing framework with pytest configuration

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to create new tasks with title and description

**Independent Test**: Can be fully tested by running the console app, entering task details, and verifying the task is created in the in-memory store.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [P] [US1] Contract test for add task functionality in tests/contract/test_task_add.py
- [ ] T010 [P] [US1] Integration test for add task user flow in tests/integration/test_add_task.py

### Implementation for User Story 1

- [x] T011 [US1] Implement add task command in src/controllers/task_controller.py
- [x] T012 [US1] Add CLI command for task creation in src/views/cli_view.py
- [x] T013 [US1] Connect add task functionality to main loop in main.py
- [x] T014 [US1] Add validation for task title and description in src/models/task.py
- [x] T015 [US1] Add error handling for empty task titles in src/controllers/task_controller.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Tasks (Priority: P2)

**Goal**: Enable users to see a list of all tasks with status indicators

**Independent Test**: Can be tested by adding some tasks and then viewing the task list to confirm they appear with correct status indicators.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T016 [P] [US2] Contract test for view tasks functionality in tests/contract/test_task_view.py
- [ ] T017 [P] [US2] Integration test for view tasks user flow in tests/integration/test_view_tasks.py

### Implementation for User Story 2

- [x] T018 [P] [US2] Implement list tasks functionality in src/repositories/task_repository.py
- [x] T019 [US2] Implement view tasks command in src/controllers/task_controller.py
- [x] T020 [US2] Add CLI command for viewing tasks in src/views/cli_view.py
- [x] T021 [US2] Format task display with status indicators in src/views/cli_view.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Complete (Priority: P3)

**Goal**: Enable users to toggle a task's status between complete/incomplete

**Independent Test**: Can be tested by creating a task, marking it complete, then verifying the status has changed.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T022 [P] [US3] Contract test for mark complete functionality in tests/contract/test_task_complete.py
- [ ] T023 [P] [US3] Integration test for mark complete user flow in tests/integration/test_mark_complete.py

### Implementation for User Story 3

- [x] T024 [US3] Implement toggle status functionality in src/repositories/task_repository.py
- [x] T025 [US3] Implement mark complete command in src/controllers/task_controller.py
- [x] T026 [US3] Add CLI command for marking tasks complete in src/views/cli_view.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task (Priority: P4)

**Goal**: Enable users to modify existing task details

**Independent Test**: Can be tested by updating a task's title or description and verifying the changes are saved.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T027 [P] [US4] Contract test for update task functionality in tests/contract/test_task_update.py
- [ ] T028 [P] [US4] Integration test for update task user flow in tests/integration/test_update_task.py

### Implementation for User Story 4

- [x] T029 [US4] Implement update task functionality in src/repositories/task_repository.py
- [x] T030 [US4] Implement update task command in src/controllers/task_controller.py
- [x] T031 [US4] Add CLI command for updating tasks in src/views/cli_view.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: Enable users to remove a task by ID

**Independent Test**: Can be tested by deleting a task and verifying it no longer appears in the task list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T032 [P] [US5] Contract test for delete task functionality in tests/contract/test_task_delete.py
- [ ] T033 [P] [US5] Integration test for delete task user flow in tests/integration/test_delete_task.py

### Implementation for User Story 5

- [x] T034 [US5] Implement delete task functionality in src/repositories/task_repository.py
- [x] T035 [US5] Implement delete task command in src/controllers/task_controller.py
- [x] T036 [US5] Add CLI command for deleting tasks in src/views/cli_view.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T037 [P] Add comprehensive error handling across all components
- [ ] T038 [P] Add logging functionality for debugging
- [x] T039 [P] Add input validation across all user inputs
- [x] T040 [P] Add help and usage documentation to CLI
- [ ] T041 [P] Run quickstart.md validation and integration testing
- [ ] T042 [P] Performance testing with 1000+ tasks

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

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
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
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