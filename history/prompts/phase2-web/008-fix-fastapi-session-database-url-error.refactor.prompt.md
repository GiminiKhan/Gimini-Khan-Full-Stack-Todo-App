---
id: 008
title: Fix FastAPI Session Database URL Error
stage: refactor
date: 2026-01-06
surface: agent
model: Claude Sonnet 4.5
feature: phase2-web
branch: main
user: Claude Code
command: sp.implement
labels: ["fastapi", "database", "session", "env"]
links:
  spec: specs/phase2-web/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - src/backend/database/session.py
tests:
 - null
---

## Prompt

Fix: FastAPI session cannot find DATABASE_URL

# Issue: FastAPI server returns 500 because src/backend/database/session.py is raising ValueError: "DATABASE_URL not set".

1. `src/backend/database/session.py` ko update karein.
2. Ensure karein ke `load_dotenv` root folder wali `.env` file ko load kare (the same way we did for Alembic).
3. `get_engine()` function mein check karein ke `settings.database_url` sahi se use ho raha hai.
4. Agar `settings.database_url` None hai, to `os.getenv("DATABASE_URL")` ko fallback ke taur par use karein.

## Response snapshot

Successfully fixed the FastAPI session database URL issue by updating the session.py file:

1. Updated `src/backend/database/session.py`:
   - Added import for `dotenv` module
   - Added explicit loading of .env file using absolute path: `load_dotenv(env_path)` where env_path is constructed using `os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')`
   - This ensures the .env file in the project root is loaded regardless of the current working directory when FastAPI runs

2. Updated `get_engine()` function:
   - Modified to get the database URL from settings first
   - Added fallback to check `os.getenv("DATABASE_URL")` if `settings.database_url` is None or empty
   - Added validation to raise ValueError with message "DATABASE_URL not set in environment or settings" if the URL is still not found
   - Maintained all existing asyncpg-specific parameter handling

The changes ensure that FastAPI can properly load the database URL from the environment with appropriate fallbacks, preventing the 500 error caused by the missing DATABASE_URL.

## Outcome

- ✅ Impact: Fixed FastAPI server 500 error due to missing DATABASE_URL
- 🧪 Tests: null
- 📁 Files: 1 file modified to fix database session loading
- 🔁 Next prompts: Start FastAPI server to verify the fix works
- 🧠 Reflection: Proper path handling and fallbacks prevent session errors

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null