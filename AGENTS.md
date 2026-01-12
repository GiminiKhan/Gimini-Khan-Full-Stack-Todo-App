# AGENTS.md - Spec-Kit Plus Agent Guide for To-Do App

## Overview
This document explains how to use the Spec-Kit Plus agents for developing and maintaining the To-Do application. The project follows Spec-Driven Development (SDD) principles using Claude Code and the nine pillars of AI-driven development.

## Available Agent Commands

### Core Spec-Kit Commands
- `/sp.specify` - Create or update feature specifications from natural language descriptions
- `/sp.plan` - Generate implementation plans based on specifications
- `/sp.tasks` - Create actionable, dependency-ordered task lists
- `/sp.implement` - Execute the implementation plan by processing tasks
- `/sp.analyze` - Perform consistency analysis across spec, plan, and tasks
- `/sp.adr` - Create Architecture Decision Records for significant decisions
- `/sp.checklist` - Generate custom checklists for features
- `/sp.clarify` - Identify underspecified areas and ask clarification questions
- `/sp.reverse-engineer` - Reverse engineer codebase into SDD-RI artifacts
- `/sp.constitution` - Create/update project constitution principles
- `/sp.phr` - Record AI exchanges as Prompt History Records

### Git Workflow Agent
- `/sp.git.commit_pr` - Intelligent git workflow for committing and creating PRs

### Issue Management
- `/sp.taskstoissues` - Convert tasks into GitHub issues

## Project Structure Reference

### Specifications Directory
```
specs/
├── 1-console-task-app/     # Phase I: Console application
│   ├── spec.md            # Console app requirements
│   ├── plan.md            # Console app architecture
│   └── tasks.md           # Console app task checklist
└── phase2-web/            # Phase II: Web application
    ├── spec.md           # Web app requirements
    ├── plan.md           # Web app architecture
    └── tasks.md          # Web app task checklist
```

### Source Code Structure
```
src/
├── frontend/              # Next.js frontend (to be implemented)
└── backend/               # FastAPI backend (currently implemented)
    ├── api/              # API routes
    ├── models/           # Database models
    ├── schemas/          # Pydantic schemas
    ├── database/         # Database connection
    ├── core/             # Core utilities
    └── tests/            # Test files
```

## Recommended Workflow

### 1. New Feature Development
```bash
# Start with specification
/sp.specify

# Generate plan
/sp.plan

# Create tasks
/sp.tasks

# Review and analyze
/sp.analyze

# Implement
/sp.implement
```

### 2. Existing Feature Enhancement
```bash
# Navigate to appropriate spec
cd specs/[feature-name]/

# Clarify requirements if needed
/sp.clarify

# Update specification
/sp.specify

# Generate new tasks
/sp.tasks

# Implement
/sp.implement
```

### 3. Architecture Decision Documentation
When making significant architectural decisions (framework choices, security implementations, database schema changes):
```bash
/sp.adr "Decision Title"
```

### 4. Code Quality and Consistency
```bash
# Analyze consistency across artifacts
/sp.analyze

# Generate custom checklists
/sp.checklist
```

## Tech Stack Agents

### Backend Development (FastAPI)
- Use `/sp.tasks` to generate backend-specific tasks
- Leverage `/sp.analyze` to check API consistency
- Use `/sp.adr` for database and authentication decisions

### Frontend Development (Next.js)
- Use `/sp.specify` to define UI requirements
- Generate component task lists with `/sp.tasks`
- Create responsive design plans with `/sp.plan`

### Database Engineering (Neon PostgreSQL)
- Document schema decisions with `/sp.adr`
- Generate migration tasks with `/sp.tasks`
- Analyze data model consistency with `/sp.analyze`

## Best Practices

### 1. Spec-First Approach
Always start with `/sp.specify` before implementing any significant feature.

### 2. Incremental Development
Use the agent commands in small increments to maintain consistency.

### 3. Documentation
Record important decisions and conversations using `/sp.phr`.

### 4. Quality Assurance
Regularly use `/sp.analyze` to maintain consistency across specifications.

## Troubleshooting

### Common Issues
- **Inconsistent specs**: Use `/sp.analyze` to identify inconsistencies
- **Missing tasks**: Use `/sp.tasks` to regenerate based on updated specs
- **Unclear requirements**: Use `/sp.clarify` to ask targeted questions

### Recovery Steps
If you encounter inconsistencies:
1. Use `/sp.reverse-engineer` to analyze current codebase
2. Update specifications with `/sp.specify`
3. Regenerate plans and tasks
4. Use `/sp.analyze` to verify consistency

## Integration with Project Goals

This agent framework supports the nine pillars of AI-driven development:
1. **Spec-Driven Development**: `/sp.specify`, `/sp.plan`, `/sp.tasks`
2. **Claude Code & Spec-Kit Plus**: All agent commands
3. **Monorepo**: Coordinated development across frontend/backend
4. **Reusable Intelligence**: Agent skill reuse
5. **Database Engineering**: Database-focused agents
6. **Authentication & Security**: Security-aware planning
7. **Cloud Native AI**: Deployment-focused workflows
8. **Iterative Evolution**: Incremental development support
9. **AI-Native Architecture**: AI-aware architectural decisions

## Quick Start Examples

### Add a new feature:
```bash
/sp.specify  # Describe your feature
/sp.plan     # Generate architecture plan
/sp.tasks    # Create implementation tasks
/sp.implement # Execute the tasks
```

### Review current state:
```bash
/sp.analyze  # Check consistency
/sp.adr "Security Update"  # Document important decisions
/sp.phr      # Record development notes
```

### Get help with existing code:
```bash
/sp.reverse-engineer  # Understand current implementation
/sp.clarify           # Get clarification on requirements
```

---

**Note**: Always ensure your specifications, plans, and tasks remain synchronized by using `/sp.analyze` regularly to verify consistency across all artifacts.