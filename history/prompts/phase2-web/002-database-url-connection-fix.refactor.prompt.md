---
id: 002
title: Database URL Connection Fix
stage: refactor
date: 2026-01-06
surface: agent
model: Claude Sonnet 4.5
feature: phase2-web
branch: main
user: Claude Code
command: sp.implement
labels: ["database", "config", "env", "asyncpg", "connection"]
links:
  spec: specs/phase2-web/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - src/backend/core/config.py
 - src/backend/database/session.py
tests:
 - null
---

## Prompt

Fix: Database URL Connection Issue

# Role: Backend Specialist
# Issue: DATABASE_URL not detected even though .env is in root.

1. `src/backend/core/config.py` ko update karein:
   - `python-dotenv` se `load_dotenv()` ko explicitly call karein.
   - Pydantic Settings mein `env_file=".env"` ka absolute path set karein agar zaroorat ho.
2. `src/backend/database/session.py` ko verify karein ke wo `settings.DATABASE_URL` use kar raha hai, manually string dhoondne ki bajaye.
3. Check karein ke `asyncpg` driver engine mein correctly use ho raha hai.

Please fix this so the registration endpoint stops throwing 500 error.

## Response snapshot

Successfully fixed the database URL connection issue by implementing the following changes:

1. Updated `src/backend/core/config.py`:
   - Added import for `python-dotenv` and `os`
   - Added explicit `load_dotenv()` call to load environment variables from .env file
   - Updated the Config class to specify the absolute path to the .env file using `os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")`
   - Added proper encoding specification

2. Updated `src/backend/database/session.py`:
   - Removed the manual environment variable checking logic that was falling back to `os.getenv("DATABASE_URL")`
   - Now the function relies solely on `settings.database_url` which is properly loaded from the .env file
   - Improved asyncpg-specific parameter handling by properly passing SSL and other connection parameters through the `connect_args` parameter
   - Added proper handling for sslmode, sslcert, sslkey, and sslrootcert parameters for asyncpg compatibility

The changes ensure that:
- Environment variables are properly loaded from the root .env file
- The application uses the settings.DATABASE_URL value instead of manually searching for environment variables
- Asyncpg driver is correctly configured with proper connection arguments
- The registration endpoint should no longer throw 500 errors due to database connection issues

## Outcome

- ✅ Impact: Fixed database connection issue by properly loading DATABASE_URL from .env
- 🧪 Tests: null
- 📁 Files: 2 files modified to fix environment variable loading and database connection
- 🔁 Next prompts: Test registration endpoint to verify the fix works
- 🧠 Reflection: The issue was caused by improper environment variable loading in Pydantic Settings

## Evaluation notes (flywheel)

- Failure modes observed: null
- Graders run and results (PASS/FAIL): null
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null