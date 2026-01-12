import { apiGet, apiPost, apiPut, apiDelete } from './api';
import { Task } from '@/types/todo';
import { getAccessToken } from './auth';

// Get all tasks for the authenticated user
export const getTasks = async (): Promise<Task[]> => {
  try {
    // Get the user ID from the stored token or context
    // For now, we'll need to get the user ID from the auth context
    // This requires the user object to be passed or accessed from context
    const token = getAccessToken();
    console.log('Access token for tasks API:', token);

    // We need to get the user ID somehow - for now let's try to extract it from localStorage
    // In a real implementation, you'd get this from the auth context
    const userStr = localStorage.getItem('user');
    let userId = '';
    if (userStr) {
      try {
        const user = JSON.parse(userStr);
        userId = user.id;
      } catch (e) {
        console.error('Error parsing user from localStorage:', e);
      }
    }

    if (!userId) {
      // If we can't get the user ID, we need to get it from the session
      // For now, let's try to extract it from the token (this is a simplified approach)
      if (token) {
        try {
          // Decode JWT token to get user ID (simplified)
          const tokenParts = token.split('.');
          if (tokenParts.length === 3) {
            const payload = JSON.parse(atob(tokenParts[1]));
            userId = payload.userId || payload.sub || payload.user_id;
          }
        } catch (e) {
          console.error('Error decoding token to get user ID:', e);
        }
      }
    }

    console.log('User ID for tasks API:', userId);

    if (!userId) {
      throw new Error('User ID is required to fetch tasks');
    }

    const response = await apiGet<Task[]>(`/api/${userId}/tasks`);
    return response.data;
  } catch (error) {
    console.error('Error fetching tasks:', error);
    throw error;
  }
};

// Create a new task
export const createTask = async (taskData: Omit<Task, 'id' | 'created_at' | 'updated_at'>): Promise<Task> => {
  try {
    // Get user ID similar to getTasks
    const token = getAccessToken();
    let userId = '';
    if (token) {
      try {
        const tokenParts = token.split('.');
        if (tokenParts.length === 3) {
          const payload = JSON.parse(atob(tokenParts[1]));
          userId = payload.userId || payload.sub || payload.user_id;
        }
      } catch (e) {
        console.error('Error decoding token to get user ID:', e);
      }
    }

    if (!userId) {
      throw new Error('User ID is required to create task');
    }

    const response = await apiPost<Task>(`/api/${userId}/tasks`, taskData);
    return response.data;
  } catch (error) {
    console.error('Error creating task:', error);
    throw error;
  }
};

// Update an existing task
export const updateTask = async (id: string, taskData: Partial<Task>): Promise<Task> => {
  try {
    // Get user ID similar to getTasks
    const token = getAccessToken();
    let userId = '';
    if (token) {
      try {
        const tokenParts = token.split('.');
        if (tokenParts.length === 3) {
          const payload = JSON.parse(atob(tokenParts[1]));
          userId = payload.userId || payload.sub || payload.user_id;
        }
      } catch (e) {
        console.error('Error decoding token to get user ID:', e);
      }
    }

    if (!userId) {
      throw new Error('User ID is required to update task');
    }

    const response = await apiPut<Task>(`/api/${userId}/tasks/${id}`, taskData);
    return response.data;
  } catch (error) {
    console.error('Error updating task:', error);
    throw error;
  }
};

// Delete a task
export const deleteTask = async (id: string): Promise<void> => {
  try {
    // Get user ID similar to getTasks
    const token = getAccessToken();
    let userId = '';
    if (token) {
      try {
        const tokenParts = token.split('.');
        if (tokenParts.length === 3) {
          const payload = JSON.parse(atob(tokenParts[1]));
          userId = payload.userId || payload.sub || payload.user_id;
        }
      } catch (e) {
        console.error('Error decoding token to get user ID:', e);
      }
    }

    if (!userId) {
      throw new Error('User ID is required to delete task');
    }

    await apiDelete(`/api/${userId}/tasks/${id}`);
  } catch (error) {
    console.error('Error deleting task:', error);
    throw error;
  }
};

// Toggle task completion status
export const toggleTaskCompletion = async (id: string, isCompleted: boolean): Promise<Task> => {
  try {
    // Get user ID similar to getTasks
    const token = getAccessToken();
    let userId = '';
    if (token) {
      try {
        const tokenParts = token.split('.');
        if (tokenParts.length === 3) {
          const payload = JSON.parse(atob(tokenParts[1]));
          userId = payload.userId || payload.sub || payload.user_id;
        }
      } catch (e) {
        console.error('Error decoding token to get user ID:', e);
      }
    }

    if (!userId) {
      throw new Error('User ID is required to toggle task completion');
    }

    const response = await apiPut<Task>(`/api/${userId}/tasks/${id}/complete?is_completed=${isCompleted}`);
    return response.data;
  } catch (error) {
    console.error('Error toggling task completion:', error);
    throw error;
  }
};