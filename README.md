# Taskify - Full-Stack Web Application

A modern full-stack web application for task management built with FastAPI (backend) and Next.js (frontend). Features secure authentication, CRUD operations, real-time search, and priority filtering.

## 🚀 Features

- **Authentication System**: Secure user registration and login with JWT tokens
- **CRUD Operations**: Create, Read, Update, and Delete tasks with full functionality
- **Real-time Search**: Instant search functionality to filter tasks by title
- **Priority Filtering**: Filter tasks by priority level (High, Medium, Low, or All)
- **Responsive UI**: Modern, clean interface built with Tailwind CSS
- **Task Management**: Complete task lifecycle with completion toggling
- **Edit Functionality**: Update task details without leaving the dashboard

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL (via Neon)
- **Authentication**: JWT-based authentication
- **ORM**: SQLModel for database modeling
- **Dependencies**: Managed with `uv` and `pyproject.toml`

### Frontend
- **Framework**: Next.js 15+ with TypeScript
- **Styling**: Tailwind CSS with Indigo & Slate theme
- **Icons**: Lucide React
- **Architecture**: Client-side rendering with React hooks

## 📁 Project Structure

```
├── backend/                 # FastAPI backend
│   ├── api/                # API routes and endpoints
│   ├── models/             # Database models (SQLModel)
│   ├── services/           # Business logic
│   ├── database/           # Database connection and configuration
│   ├── core/               # Core utilities and security
│   └── main.py             # Application entry point
├── frontend/              # Next.js frontend
│   ├── app/               # Next.js 13+ app router
│   │   ├── dashboard/     # Dashboard page with task management
│   │   ├── login/         # Login page
│   │   ├── register/      # Registration page
│   │   ├── globals.css    # Global styles
│   │   └── layout.tsx     # Root layout
│   ├── components/        # Reusable UI components
│   ├── services/          # API clients and utilities
│   └── public/            # Static assets
├── specs/                 # Specification files
└── README.md             # This file
```

## 🏗️ Setup Instructions

### Prerequisites
- Node.js (v18 or higher)
- Python 3.11+
- PostgreSQL database (or Neon account)
- `uv` package manager (recommended) or `pip`

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials and secret keys
```

4. Run database migrations:
```bash
# If using alembic for migrations
alembic upgrade head
```

5. Start the backend server:
```bash
uv run main.py
# Or
python main.py
```

The backend will start on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
# or
pnpm install
```

3. Set up environment variables:
```bash
cp .env.example .env.local
# Edit .env.local with your backend API URL
```

4. Start the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

The frontend will start on `http://localhost:3000`

## 🚀 Running the Application

### Development
1. Start the backend server in the `backend/` directory:
```bash
uv run main.py
```

2. In a separate terminal, start the frontend in the `frontend/` directory:
```bash
npm run dev
```

3. Open your browser to `http://localhost:3000`

### Production
1. Build the frontend:
```bash
cd frontend && npm run build
```

2. Serve the backend with a production ASGI server like Uvicorn:
```bash
cd backend && uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🌐 API Endpoints

The backend provides the following REST API endpoints:

- `GET /api/{user_id}/tasks` - Get all user tasks
- `POST /api/{user_id}/tasks` - Create a new task
- `PUT /api/{user_id}/tasks/{task_id}` - Update a task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{task_id}/complete` - Toggle task completion
- `POST /auth/login` - User login
- `POST /auth/register` - User registration

## 🔐 Authentication

The application uses JWT-based authentication:
- Users must register and login to access the dashboard
- Authentication tokens are stored in localStorage
- Protected routes are guarded by authentication middleware

## 💡 Key Features Explained

### Real-time Search
- Search tasks by title as you type
- Results update instantly without page refresh
- Case-insensitive search functionality

### Priority Filtering
- Filter tasks by priority level (High, Medium, Low, or All)
- Case-insensitive comparison between UI and database values
- Dynamic filtering updates the task list immediately

### Task Management
- Create new tasks with title, description, and priority
- Update existing tasks with inline editing
- Mark tasks as complete/incomplete with one click
- Delete tasks with confirmation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🐛 Issues

If you encounter any issues or bugs, please open an issue in the GitHub repository with detailed information about the problem and steps to reproduce it.