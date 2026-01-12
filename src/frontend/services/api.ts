import axios from 'axios';
import { useSession } from '@/lib/auth/client';

// Create an Axios instance with default configuration
const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
  timeout: 10000, // 10 seconds timeout
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add Better Auth token if available
apiClient.interceptors.request.use(
  (config) => {
    // For Better Auth, we'll need to get the session token differently
    // This is a simplified approach - in a real app, you might need to use
    // Better Auth's session management to get the current token
    try {
      // Attempt to get Better Auth session token
      // Note: Better Auth typically handles this automatically with cookies
      // For API calls that need the token in headers, we might need to get it from the session
      const token = typeof window !== 'undefined' ? localStorage.getItem('better-auth.session_token') : null;
      if (token && config.headers) {
        config.headers.Authorization = `Bearer ${token}`;
      }
    } catch (error) {
      console.error('Error getting Better Auth token:', error);
    }

    return config;
  },
  (error: any) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle common errors
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error: any) => {
    // Handle specific error cases here
    if (error.response?.status === 401) {
      // Session might be expired, redirect to login
      localStorage.removeItem('better-auth.session_token');
      if (typeof window !== 'undefined') {
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export default apiClient;

// Export utility functions for common HTTP methods
export const apiGet = async <T>(url: string, config?: any): Promise<any> => {
  return await apiClient.get<T>(url, config);
};

export const apiPost = async <T>(url: string, data?: any, config?: any): Promise<any> => {
  return await apiClient.post<T>(url, data, config);
};

export const apiPut = async <T>(url: string, data?: any, config?: any): Promise<any> => {
  return await apiClient.put<T>(url, data, config);
};

export const apiDelete = async <T>(url: string, config?: any): Promise<any> => {
  return await apiClient.delete<T>(url, config);
};