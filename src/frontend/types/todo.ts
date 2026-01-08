// Task interface definition
export interface Task {
  id: string;
  title: string;
  description?: string;
  is_completed: boolean;
  created_at: string; // ISO string format
  updated_at: string; // ISO string format
  due_date?: string; // Optional due date in ISO string format
  priority?: 'low' | 'medium' | 'high'; // Optional priority level
  category?: string; // Optional category
  owner_id?: string; // Optional owner ID
}

// Interface for creating a new task (without id and timestamps)
export interface CreateTaskData {
  title: string;
  description?: string;
  is_completed?: boolean;
  due_date?: string;
  priority?: 'low' | 'medium' | 'high';
  category?: string;
}

// Interface for updating a task (all fields optional)
export interface UpdateTaskData {
  title?: string;
  description?: string;
  is_completed?: boolean;
  due_date?: string;
  priority?: 'low' | 'medium' | 'high';
  category?: string;
}

// Interface for API response when fetching tasks
export interface GetTasksResponse {
  tasks: Task[];
  total: number;
  page: number;
  limit: number;
}