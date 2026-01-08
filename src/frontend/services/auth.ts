import { apiPost, apiGet } from './api';

interface User {
  id: string;
  email: string;
  full_name?: string;
  is_active: boolean;
}

interface LoginCredentials {
  email: string;
  password: string;
}

interface RegisterData {
  email: string;
  password: string;
  full_name?: string;
}

interface AuthResponse {
  access_token: string;
  token_type: string;
}

// Register a new user
export const registerUser = async (userData: RegisterData): Promise<User> => {
  try {
    const response = await apiPost<User>('/auth/register', userData);
    return response.data;
  } catch (error) {
    console.error('Registration error:', error);
    throw error;
  }
};

// Login user and get access token
export const loginUser = async (credentials: LoginCredentials): Promise<AuthResponse> => {
  try {
    // For login, we need to send credentials to the token endpoint
    // Using form data as FastAPI OAuth2PasswordRequestForm expects
    const formData = new FormData();
    formData.append('username', credentials.email);
    formData.append('password', credentials.password);

    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/auth/token`, {
      method: 'POST',
      body: formData,
      headers: {
        // Don't include Content-Type header when using FormData
        // It will be set automatically with the correct boundary
      },
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || 'Login failed');
    }

    const data: AuthResponse = await response.json();
    return data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
};

// Alternative login method using apiPost if form data approach doesn't work
export const loginUserAlt = async (credentials: LoginCredentials): Promise<AuthResponse> => {
  try {
    // Alternative approach using application/x-www-form-urlencoded
    const params = new URLSearchParams();
    params.append('username', credentials.email);
    params.append('password', credentials.password);

    const response = await apiPost<AuthResponse>('/auth/token', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });

    return response.data;
  } catch (error) {
    console.error('Login error:', error);
    throw error;
  }
};

// Check if user is authenticated
export const checkAuthStatus = async (): Promise<User | null> => {
  try {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      return null;
    }

    const response = await apiGet<User>('/users/me');
    return response.data;
  } catch (error) {
    console.error('Auth status check error:', error);
    localStorage.removeItem('accessToken');
    return null;
  }
};

// Logout user
export const logoutUser = (): void => {
  localStorage.removeItem('accessToken');
  // Optionally redirect to login page
  // window.location.href = '/login';
};

// Save access token to localStorage
export const saveAccessToken = (token: string): void => {
  localStorage.setItem('accessToken', token);
};

// Get access token from localStorage
export const getAccessToken = (): string | null => {
  return localStorage.getItem('accessToken');
};