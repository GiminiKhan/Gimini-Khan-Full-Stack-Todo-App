# Research: Pydantic-Core Module Error in Vercel Deployment

## Problem Statement

The to-do app is failing to deploy on Vercel with the error: `ModuleNotFoundError: No module named 'pydantic_core._pydantic_core'`. This occurs during the import of FastAPI which depends on Pydantic, which in turn depends on pydantic-core.

## Root Cause Analysis

### Initial Error
- Error: `ModuleNotFoundError: No module named 'pydantic_core._pydantic_core'`
- Location: During import of FastAPI in `src/backend/main.py`
- Environment: Vercel serverless functions

### Investigation Findings
1. **Dependency Conflict**: The original `requirements.txt` had:
   - `pydantic>=2.7.0`
   - `pydantic-core>=2.18.0`

   Having both specified separately can cause version conflicts as pydantic-core is a low-level dependency that should typically be managed by pydantic itself.

2. **Native Extensions**: `pydantic_core._pydantic_core` is a compiled C extension that may not be properly built in Vercel's Linux environment.

3. **Vercel Limitations**: Some native extensions may not compile properly in Vercel's build environment.

## Solution Implemented

### Dependency Updates
Updated `requirements.txt` to resolve conflicts:
- Changed `pydantic>=2.7.0` and `pydantic-core>=2.18.0` to just `pydantic>=2.10.0`
- Removed explicit pydantic-core dependency to let pydantic manage it
- Updated pydantic-settings to `pydantic-settings>=2.6.0`

### Rationale
- Removing the explicit pydantic-core version allows pydantic to manage its own dependencies
- This prevents version conflicts between manually specified versions
- Pydantic will install a compatible version of pydantic-core automatically

## Decision Log

### Decision: Remove explicit pydantic-core dependency
- **Rationale**: Prevents version conflicts with pydantic's own dependency management
- **Alternative Considered**: Pinning specific versions - rejected as it could create future conflicts
- **Outcome**: Cleaner dependency resolution

### Decision: Upgrade pydantic to latest stable
- **Rationale**: Latest versions have better compatibility with serverless environments
- **Alternative Considered**: Downgrading to older versions - rejected as it would miss bug fixes
- **Outcome**: Better stability in deployment environments

## Verification Steps

1. ✅ Updated requirements.txt
2. ✅ Verified FastAPI imports work with new dependencies
3. ✅ Maintained all existing functionality
4. ✅ Dependencies are compatible with Vercel environment