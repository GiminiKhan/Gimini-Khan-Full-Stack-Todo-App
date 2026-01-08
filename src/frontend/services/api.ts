import axios from 'axios';

// Create an Axios instance with default configuration
const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000/api/v1',
  timeout: 10000, // 10 seconds timeout
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token if available
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('accessToken');
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`;
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
      // Token might be expired, redirect to login
      localStorage.removeItem('accessToken');
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