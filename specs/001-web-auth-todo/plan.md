# Implementation Plan: Web Authentication and Todo Management

**Branch**: `001-web-auth-todo` | **Date**: 2026-01-20 | **Spec**: [link](./spec.md)
**Input**: Feature specification from `/specs/001-web-auth-todo/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a complete web authentication system and todo management application with Better Auth integration, secure API endpoints, and modern UI with Indigo & Slate theme. The solution follows cloud-native architecture with FastAPI backend, Neon PostgreSQL database, and Next.js 15+ frontend with Tailwind CSS.

Additionally, this plan includes a critical security fix to replace hardcoded fake tokens in the authentication service with real JWT tokens using the existing create_access_token function.

## Technical Context

**Language/Version**: Python 3.11 (Backend), JavaScript/TypeScript (Frontend)
**Primary Dependencies**: FastAPI, Next.js 15+, Better Auth, Neon PostgreSQL, Tailwind CSS, SQLAlchemy
**Storage**: Neon PostgreSQL (Cloud-native SQL database)
**Testing**: pytest (Backend), Jest/Cypress (Frontend)
**Target Platform**: Web application (SSR/CSR with Next.js)
**Project Type**: Web application (separate frontend and backend)
**Performance Goals**: Sub-200ms API response times, 95% uptime, 5-second dashboard load time
**Constraints**: JWT token security, user data isolation, GDPR compliance
**Scale/Scope**: Support 10k+ concurrent users, responsive design for all screen sizes

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Spec-Driven Development (SDD)
- [X] All features and changes must be specified before implementation begins
- [X] Clear requirements and acceptance criteria must be documented in spec.md

### No Manual Code
- [X] All code must be generated through Claude Code or integrated agents
- [X] No manual code writing is permitted
- [X] Implementation must follow automated generation processes

### Agentic Stack
- [X] Technology stack utilizes UV, Python 3.13+, and Claude Code as required components
- [X] Agentic approach ensures automation and consistency across development lifecycle

### Clean Architecture
- [X] Codebase maintains modular and clean architecture principles using Cloud-Native Architecture (FastAPI + Neon PostgreSQL)
- [X] Architecture ensures maintainability, testability, scalability, and robust data persistence

### Process Integrity
- [X] Every code change references a Task ID before implementation
- [X] Traceability and accountability maintained throughout development process

### Security Protocol
- [X] Better Auth with JWT implemented as mandatory security protocol for all authentication and authorization flows
- [X] Secure user access, token management, and protection of sensitive data across all application layers

### Frontend Standard
- [X] Next.js 15+ App Router used as the standard for all frontend development
- [X] Modern React development practices, server-side rendering capabilities, and optimized performance ensured

### UI/UX Standards
- [X] Modern & Attractive UI implemented using Tailwind CSS with Indigo/Slate theme
- [X] Consistent visual identity, responsive design, accessibility compliance, and enhanced user experience maintained

## Project Structure

### Documentation (this feature)

```text
specs/001-web-auth-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── todo.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── todo_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   ├── auth.py
│   │   └── todos.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── security.py
│   │   └── exceptions.py
│   └── main.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_auth.py
    └── test_todos.py

frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── auth/
│   │   │   ├── login/
│   │   │   │   └── page.tsx
│   │   │   └── logout/
│   │   │       └── page.tsx
│   │   └── dashboard/
│   │       └── page.tsx
│   ├── components/
│   │   ├── ui/
│   │   │   ├── skeleton-loader.tsx
│   │   │   ├── todo-card.tsx
│   │   │   └── auth-guard.tsx
│   │   ├── layouts/
│   │   │   └── protected-layout.tsx
│   │   └── forms/
│   │       └── todo-form.tsx
│   ├── services/
│   │   ├── api-client.ts
│   │   ├── auth-client.ts
│   │   └── todo-client.ts
│   ├── lib/
│   │   ├── utils.ts
│   │   └── constants.ts
│   └── styles/
│       └── globals.css
├── public/
├── next.config.js
├── tailwind.config.js
├── postcss.config.js
├── package.json
└── tsconfig.json

tests/
├── contract/
│   └── todo_api_contract_test.py
├── integration/
│   └── auth_integration_test.py
└── unit/
    └── todo_unit_test.py
```

**Structure Decision**: Web application with separate backend (FastAPI) and frontend (Next.js) following cloud-native architecture principles with proper separation of concerns.

## Authentication Token Fix Details

### Affected Files
- `backend/src/services/auth_service.py` - Contains hardcoded fake token that needs replacement
- `backend/src/core/security.py` - Contains the create_access_token function to be used

### Change Description
- Replace the fake token generation (`f'fake-token-{user.id}'`) with a real JWT token using `create_access_token()` function
- Include proper user identification in the token payload
- Maintain the same API contract while improving security

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | | |
