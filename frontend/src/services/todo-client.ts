import { apiClient } from './api-client';

class TodoService {
  async getTodos(): Promise<any[]> {
    return await apiClient.get('/todos/');
  }

  async createTodo(todoData: any): Promise<any> {
    return await apiClient.post('/todos/', todoData);
  }

  async updateTodo(id: string, todoData: any): Promise<any> {
    return await apiClient.patch(`/todos/${id}`, todoData);
  }

  async deleteTodo(id: string): Promise<void> {
    return await apiClient.delete(`/todos/${id}`);
  }
}

export const todoService = new TodoService();