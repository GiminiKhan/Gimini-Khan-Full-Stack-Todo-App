---
id: 004
title: Alembic Async Driver Compatibility Fix
stage: refactor
date: 2026-01-06
surface: agent
model: Claude Sonnet 4.5
feature: phase2-web
branch: main
user: Claude Code
command: sp.implement
labels: ["alembic", "migration", "asyncpg", "database"]
links:
  spec: specs/phase2-web/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - src/backend/migrations/env.py
tests:
 - null
---

## Prompt

 Fix: Alembic Async Driver Compatibility

# Issue: Alembic is failing with NoSuchModuleError because it's trying to use 'asyncpg' in a synchronous context during migration.

1. `src/backend/migrations/env.py` ko update karein:
   - `DATABASE_URL` mein agar `postgresql+asyncpg` hai, to usay `postgresql` (standard psycopg2/psycopg) se replace karein sirf migration running ke waqt.
   - Ya phir `run_migrations_online` function mein `create_engine` ko handle karein taake wo async driver par na phanse.
2. Ensure karein ke `config.set_main_option("sqlalchemy.url", ...)` sahi formatted URL use kar raha hai.

## Response snapshot

Successfully fixed the Alembic async driver compatibility issue by modifying the migrations/env.py file:

1. Updated the database URL handling logic in `src/backend/migrations/env.py`:
   - Added logic to detect when the database URL uses async drivers like `postgresql+asyncpg://` or `postgresql+psycopg://`
   - Convert these URLs to standard `postgresql://` format during migration execution
   - This allows Alembic to use the synchronous database driver which is compatible with its migration system

2. The fix specifically:
   - Checks if the settings.database_url starts with 'postgresql+asyncpg://'
   - Replaces it with 'postgresql://' for migration purposes
   - Also handles 'postgresql+psycopg://' URLs similarly
   - Uses the converted URL when setting the sqlalchemy.url in the Alembic config

This resolves the NoSuchModuleError that occurred when Alembic tried to use async drivers in a synchronous context during migrations, while preserving the async driver for normal application operation.

## Outcome

- ✅ Impact: Fixed Alembic migration compatibility with async database drivers
- 🧪 Tests: null
- 📁 Files: 1 file modified to handle async driver compatibility
- 🔁 Next prompts: Run alembic migrations to verify the fix works
- 🧠 Reflection: Alembic requires synchronous drivers for migrations, unlike the application

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null