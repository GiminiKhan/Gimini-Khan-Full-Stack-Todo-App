# Quickstart Guide: Web Authentication and Todo Management

## Prerequisites

## Authentication Token Fix Implementation

### Overview
This section covers the implementation of the authentication token fix to replace hardcoded fake tokens with real JWT tokens.

### Files to Modify
1. `backend/src/services/auth_service.py` - Update the authenticate_user method

### Implementation Steps

#### Step 1: Import Required Functions
Add the import for the create_access_token function:
```python
from ..core.security import create_access_token
from datetime import timedelta
```

#### Step 2: Update the authenticate_user Method
Replace the fake token generation in the authenticate_user method:

**Before:**
```python
return {
    'access_token': f'fake-token-{user.id}',
    'token_type': 'bearer',
    'user': user
}
```

**After:**
```python
# Prepare token data with user information
token_data = {
    "sub": str(user.id),
    "email": user.email,
    "name": user.name
}

# Create access token with proper expiration
access_token = create_access_token(
    data=token_data,
    expires_delta=timedelta(minutes=30)  # Uses default from settings
)

return {
    'access_token': access_token,
    'token_type': 'bearer',
    'user': user
}
```

#### Step 3: Testing
1. Run the existing authentication tests to ensure no regression
2. Verify that the returned token is a valid JWT
3. Confirm that the token can be decoded and verified

### Verification
After implementation:
- Authentication responses should return real JWT tokens instead of fake tokens
- Tokens should contain user information in the payload
- Tokens should expire according to the configured timeout
- All existing API contracts remain unchanged

### Rollback Plan
If issues arise:
- Revert the changes in `auth_service.py`
- Restore the original fake token implementation temporarily
- Investigate the root cause before attempting the fix again

## Original Prerequisites
- Node.js 18+ for frontend
- Python 3.11+ for backend
- UV package manager
- Neon PostgreSQL database
- Better Auth configured

## Environment Setup

### Backend Setup
1. Install Python dependencies:
```bash
uv pip install fastapi uvicorn sqlalchemy asyncpg python-multipart python-jose[cryptography] passlib[bcrypt] better-exceptions
```

2. Set up environment variables:
```bash
# .env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/todo_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

3. Run database migrations:
```bash
# Create and run migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Frontend Setup
1. Install Node.js dependencies:
```bash
npm install next@latest react react-dom @heroicons/react @tailwindcss/forms
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

2. Configure Tailwind CSS for Indigo & Slate theme:
```js
// tailwind.config.js
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        slate: {
          50: '#f8fafc',
          100: '#f1f5f9',
          200: '#e2e8f0',
          300: '#cbd5e1',
          400: '#94a3b8',
          500: '#64748b',
          600: '#475569',
          700: '#334155',
          800: '#1e293b',
          900: '#0f172a',
        },
        indigo: {
          50: '#eef2ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          300: '#a5b4fc',
          400: '#818cf8',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
          800: '#3730a3',
          900: '#312e81',
        }
      }
    },
  },
  plugins: [],
}
```

## Running the Application

### Backend
```bash
# Start the backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
# Start the frontend development server
npm run dev
```

## Key Endpoints

### Authentication
- `GET /auth/login` - Login page
- `POST /auth/login` - Login submission
- `POST /auth/logout` - Logout
- `GET /dashboard` - Protected dashboard

### API Endpoints
- `GET /api/todos` - Get user's todos
- `POST /api/todos` - Create new todo
- `PATCH /api/todos/{id}` - Update todo
- `DELETE /api/todos/{id}` - Delete todo

## Testing the Application

1. Navigate to the root URL (http://localhost:3000)
2. You should be redirected to `/auth/login`
3. Log in with valid credentials
4. You should be redirected to `/dashboard`
5. Test creating, updating, and deleting todos
6. Verify that priority indicators display in correct colors (Red=High, Amber=Medium, Blue=Low)
7. Check that skeleton loaders appear during data loading

## API Testing
Use the following curl commands to test the API directly:

```bash
# Get todos (replace TOKEN with actual JWT token)
curl -H "Authorization: Bearer TOKEN" http://localhost:8000/api/todos

# Create todo
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" \
  -d '{"title":"Test Todo","description":"Test Description","priority":"high"}' \
  http://localhost:8000/api/todos

# Update todo
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer TOKEN" \
  -d '{"completed":true}' \
  http://localhost:8000/api/todos/{todo-id}

# Delete todo
curl -X DELETE -H "Authorization: Bearer TOKEN" \
  http://localhost:8000/api/todos/{todo-id}
```