<!--
SYNC IMPACT REPORT:
Version change: 1.0.0 → 2.0.0
Modified principles:
  - IV. Clean Architecture: Updated from 'in-memory storage' to 'Cloud-Native Architecture'
  - VI. Security Protocol: Added 'Better Auth with JWT' as mandatory security protocol
  - VII. Frontend Standard: Added 'Next.js 15+ App Router' as frontend standard
  - VIII. UI/UX Standards: Added 'Modern & Attractive UI' using Tailwind CSS (Indigo/Slate theme)
Added sections: Security Protocol, Frontend Standard, UI/UX Standards
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: Update all templates to reflect new principles
-->
# Evolution of Todo - Phase II Constitution

## Core Principles

### I. Spec-Driven Development (SDD)
Spec-Driven Development is the foundational approach for all development activities. All features and changes must be specified before implementation begins, ensuring clear requirements and acceptance criteria.

### II. No Manual Code
All code must be generated through Claude Code or integrated agents. No manual code writing is permitted. This ensures consistency, quality, and adherence to established patterns and practices.

### III. Agentic Stack
The technology stack must utilize UV, Python 3.13+, and Claude Code as required components. This agentic approach ensures automation and consistency across the development lifecycle.

### IV. Clean Architecture
The codebase must maintain modular and clean architecture principles using Cloud-Native Architecture (FastAPI + Neon PostgreSQL). This ensures maintainability, testability, scalability, and robust data persistence across the system.

### V. Process Integrity
Every code change must reference a Task ID before implementation. This ensures traceability, accountability, and proper change management throughout the development process.

### VI. Security Protocol
Better Auth with JWT must be implemented as the mandatory security protocol for all authentication and authorization flows. This ensures secure user access, token management, and protection of sensitive data across all application layers.

### VII. Frontend Standard
Next.js 15+ App Router must be used as the standard for all frontend development. This ensures modern React development practices, server-side rendering capabilities, optimized performance, and consistent routing patterns across the application.

### VIII. UI/UX Standards
Modern & Attractive UI must be implemented using Tailwind CSS with Indigo/Slate theme instead of simple black & white designs. This ensures consistent visual identity, responsive design, accessibility compliance, and enhanced user experience across all interfaces.

## Development Workflow
All development activities must follow the Spec-Driven Development methodology. Features must be fully specified in a spec document before any implementation work begins. This includes acceptance criteria, edge cases, and testing requirements. The workflow must incorporate cloud-native architecture considerations, security protocols, and modern UI/UX standards as mandatory elements of all feature specifications.

## Quality Standards
Code quality is maintained through automated generation, consistent architecture patterns, strict process adherence, and compliance with cloud-native best practices. All code must pass through the Claude Code generation process to ensure compliance with architectural standards, security protocols, and UI/UX guidelines. Automated testing must cover authentication flows, database interactions, and responsive UI components.

## Governance
This constitution supersedes all other development practices and guidelines. Any amendments to this constitution must be documented, approved, and include a migration plan for existing code and processes. All pull requests and code reviews must verify compliance with these principles, particularly regarding cloud-native architecture, security protocols, frontend standards, and UI/UX requirements. Migration from Phase I to Phase II principles must be completed systematically with appropriate testing and validation procedures in place.

**Version**: 2.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2026-01-20
