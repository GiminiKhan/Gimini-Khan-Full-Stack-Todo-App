---
id: "001"
title: "Switch to Direct Bcrypt"
stage: "general"
date_iso: "2026-01-07"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "main"
user: "Qurra Tul Ain"
command: "sp.implement"
labels:
  - "security"
  - "password"
  - "bcrypt"
  - "passlib"
links:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
files_yaml: |
  - F:\to-do-app\src\backend\core\security.py
  - F:\to-do-app\test_bcrypt_functionality.py
  - F:\to-do-app\test_bcrypt_comprehensive.py
tests_yaml: |
  - test_bcrypt_functionality.py
  - test_bcrypt_comprehensive.py
  - test_app.py
prompt_text: |
  Switch to Direct Bcrypt

  # Context: Passlib is causing 72-byte issues. We just installed bcrypt 4.0.1.
  1. `src/backend/core/security.py` mein `passlib` ko nikal dein.
  2. `import bcrypt` karein.
  3. `get_password_hash` function ko aise update karein:
     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
  4. `verify_password` function ko aise update karein:
     return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
response_text: |
  Successfully switched from Passlib to direct bcrypt implementation in the security module.
  - Removed Passlib import and context
  - Added bcrypt import
  - Updated get_password_hash to use bcrypt.hashpw with proper 72-byte limit handling
  - Updated verify_password to use bcrypt.checkpw with proper 72-byte limit handling
  - Maintained backward compatibility by keeping the same function signatures
  - Added comprehensive tests to verify functionality
outcome: |
  The implementation successfully replaced Passlib with direct bcrypt usage while maintaining
  the same API. The 72-byte limit issue is handled by pre-hashing long passwords with SHA-256
  before bcrypt processing, which maintains the same behavior as the original implementation.
evaluation: |
  All tests pass, including edge cases with long passwords exceeding the 72-byte limit.
  The auth system continues to work correctly with the updated security functions.
---

# Switch to Direct Bcrypt Implementation

## Summary

Switched the password hashing implementation in `src/backend/core/security.py` from using Passlib to direct bcrypt usage. This resolves the 72-byte limit issues that Passlib was causing while maintaining the same API and functionality.

## Changes Made

1. **Removed Passlib dependencies**:
   - Removed `from passlib.context import CryptContext`
   - Removed `pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")`

2. **Added bcrypt import**:
   - Added `import bcrypt`

3. **Updated `get_password_hash` function**:
   - Changed from `pwd_context.hash(password)` to `bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')`
   - Preserved the 72-byte limit workaround using SHA-256 pre-hashing

4. **Updated `verify_password` function**:
   - Changed from `pwd_context.verify(plain_password, hashed_password)` to `bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))`
   - Preserved the 72-byte limit workaround using SHA-256 pre-hashing

## Backward Compatibility

The function signatures remain unchanged, so all existing code that imports and uses these functions continues to work without modification.

## Testing

Created comprehensive tests to verify:
- Basic password hashing and verification
- Passwords of various lengths (including those exceeding 72 bytes)
- Edge cases and error conditions
- Hash consistency (different hashes for same password due to random salt)
- Integration with existing auth system

All tests pass successfully, confirming that the implementation works correctly.