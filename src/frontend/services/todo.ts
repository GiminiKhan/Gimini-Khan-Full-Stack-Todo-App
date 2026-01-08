import { apiGet, apiPost, apiPut, apiDelete } from './api';
import { Task } from '@/types/todo';

// Get all tasks for the authenticated user
export const getTasks = async (): Promise<Task[]> => {
  try {
    const response = await apiGet<Task[]>('/todos');
    return response.data;
  } catch (error) {
    console.error('Error fetching tasks:', error);
    throw error;
  }
};

// Create a new task
export const createTask = async (taskData: Omit<Task, 'id' | 'created_at' | 'updated_at'>): Promise<Task> => {
  try {
    const response = await apiPost<Task>('/todos', taskData);
    return response.data;
  } catch (error) {
    console.error('Error creating task:', error);
    throw error;
  }
};

// Update an existing task
export const updateTask = async (id: string, taskData: Partial<Task>): Promise<Task> => {
  try {
    const response = await apiPut<Task>(`/todos/${id}`, taskData);
    return response.data;
  } catch (error) {
    console.error('Error updating task:', error);
    throw error;
  }
};

// Delete a task
export const deleteTask = async (id: string): Promise<void> => {
  try {
    await apiDelete(`/todos/${id}`);
  } catch (error) {
    console.error('Error deleting task:', error);
    throw error;
  }
};

// Toggle task completion status
export const toggleTaskCompletion = async (id: string, isCompleted: boolean): Promise<Task> => {
  try {
    const response = await apiPut<Task>(`/todos/${id}/toggle`, { is_completed: isCompleted });
    return response.data;
  } catch (error) {
    console.error('Error toggling task completion:', error);
    throw error;
  }
};