# Backend API Documentation

This directory contains the FastAPI backend for the Todo application.

## API Endpoints

### Authentication
- `/api/auth/register` - User registration
- `/api/auth/login` - User login
- `/api/auth/session` - Get current session

### Tasks Management
- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task

### Projects Management
- `GET /api/{user_id}/projects` - Get all projects for a user
- `POST /api/{user_id}/projects` - Create a new project
- `GET /api/{user_id}/projects/{id}` - Get a specific project
- `PUT /api/{user_id}/projects/{id}` - Update a project
- `DELETE /api/{user_id}/projects/{id}` - Delete a project

## Technologies Used
- FastAPI
- SQLModel
- Neon PostgreSQL
- Better Auth for authentication