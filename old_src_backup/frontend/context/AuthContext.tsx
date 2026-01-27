'use client';

import { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { checkAuthStatus, logoutUser } from '@/services/auth';

interface User {
  id: string;
  email: string;
  full_name?: string;
  is_active: boolean;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (userData: User, token: string) => void;
  logout: () => void;
  checkAuth: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export function AuthProvider({ children }: AuthProviderProps) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // Check authentication status on initial load
  useEffect(() => {
    const initAuth = async () => {
      try {
        const userData = await checkAuthStatus();
        if (userData) {
          setUser(userData);
        }
      } catch (error) {
        console.error('Auth initialization error:', error);
        // Clear any invalid token
        logoutUser();
      } finally {
        setLoading(false);
      }
    };

    initAuth();
  }, []);

  const login = (userData: User, token: string) => {
    // Save token to localStorage
    localStorage.setItem('accessToken', token);
    setUser(userData);
  };

  const logout = () => {
    logoutUser(); // This also clears localStorage
    setUser(null);
  };

  const checkAuth = async () => {
    try {
      const userData = await checkAuthStatus();
      if (userData) {
        setUser(userData);
        return;
      }
      // If no user data, clear current user
      setUser(null);
    } catch (error) {
      console.error('Auth check error:', error);
      setUser(null);
    }
  };

  const value = {
    user,
    loading,
    login,
    logout,
    checkAuth,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}