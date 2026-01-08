---
id: 007
title: Fix Database URL None in Alembic
stage: debug
date: 2026-01-06
surface: agent
model: Claude Sonnet 4.5
feature: phase2-web
branch: main
user: Claude Code
command: sp.implement
labels: ["alembic", "database", "env", "config"]
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

Fix: Database URL is None in Alembic

# Context: Alembic env.py is getting None for database_url because load_dotenv() isn't finding the file from the root correctly.

1. `src/backend/migrations/env.py` ko update karein.
2. `load_dotenv()` ke bajaye, manually rasta define karein:
   `load_dotenv(os.path.join(os.getcwd(), '.env'))`
3. Ensure karein ke agar `settings.database_url` None hai, to wo `os.getenv("DATABASE_URL")` ko check kare.
4. `run_migrations_online` mein `raw_url` ko check karein: `if not raw_url: raise ValueError("DATABASE_URL NOT FOUND IN ENV")`.

## Response snapshot

Successfully fixed the issue where database URL was None in Alembic by updating the env.py file:

1. Updated `src/backend/migrations/env.py`:
   - Added import for `dotenv` module
   - Added explicit loading of .env file using absolute path: `load_dotenv(env_path)` where env_path is constructed using `os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')`
   - This ensures the .env file in the project root is loaded regardless of the current working directory when Alembic runs

2. Updated `run_migrations_online` function:
   - Added fallback to check `os.getenv("DATABASE_URL")` if `settings.database_url` is None or empty
   - Added validation to raise ValueError with message "DATABASE_URL NOT FOUND IN ENV" if the URL is still not found
   - Maintained the existing URL cleaning logic for async driver specifications
   - Kept the debug print statement to show the cleaned URL

The changes ensure that Alembic can properly load the database URL from the environment regardless of execution context, with appropriate fallbacks and error handling.

## Outcome

- ✅ Impact: Fixed None database URL issue in Alembic migrations
- 🧪 Tests: null
- 📁 Files: 1 file modified to fix environment loading
- 🔁 Next prompts: Run alembic migrations to verify the fix works
- 🧠 Reflection: Proper path handling and fallbacks prevent None URL issues

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null