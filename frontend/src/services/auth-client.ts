import { apiClient } from './api-client';

class AuthService {
  async login(email: string, password: string): Promise<any> {
    // For this implementation, we'll make a direct fetch request since auth might not use the same client
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        username: email, // FastAPI expects 'username' by default for login
        password: password,
      }),
    });

    if (!response.ok) {
      const errorData = await response.text();
      throw new Error(`Login failed: ${errorData}`);
    }

    return await response.json();
  }

  async register(email: string, name: string, password: string): Promise<any> {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/auth/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email,
        name,
        password,
      }),
    });

    if (!response.ok) {
      const errorData = await response.text();
      throw new Error(`Registration failed: ${errorData}`);
    }

    return await response.json();
  }

  async logout(): Promise<void> {
    // Clear the token from localStorage
    if (typeof window !== 'undefined') {
      localStorage.removeItem('access_token');
    }

    // Optionally call backend logout endpoint if needed
    try {
      await apiClient.post('/auth/logout');
    } catch (error) {
      // Even if backend logout fails, we still clear the local token
      console.warn('Logout endpoint failed, but clearing local token anyway');
    }
  }

  async getCurrentUser(): Promise<any> {
    return await apiClient.get('/auth/me');
  }

  isAuthenticated(): boolean {
    if (typeof window === 'undefined') {
      return false;
    }
    const token = localStorage.getItem('access_token');
    return !!token;
  }
}

export const authService = new AuthService();