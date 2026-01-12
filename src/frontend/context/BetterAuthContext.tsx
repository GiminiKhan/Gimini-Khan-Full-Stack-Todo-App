'use client';

import { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { useSession, signOut } from '@/lib/auth/client';

interface User {
  id: string;
  email: string;
  name?: string;
  emailVerified: boolean;
  image?: string;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  isAuthenticated: boolean;
  login: () => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export function BetterAuthProvider({ children }: AuthProviderProps) {
  const { data: session, isLoading } = useSession();
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!isLoading) {
      if (session?.user) {
        // Map the Better Auth session user to our User interface
        const mappedUser: User = {
          id: session.user.id,
          email: session.user.email,
          name: session.user.name || session.user.email.split('@')[0],
          emailVerified: session.user.emailVerified || false,
          image: session.user.image || undefined,
        };
        setUser(mappedUser);
      } else {
        setUser(null);
      }
      setLoading(false);
    }
  }, [session, isLoading]);

  const login = () => {
    // For Better Auth, login is handled by the signIn function from the client
    // We'll expose this differently in the context
    console.log('Login initiated through Better Auth');
  };

  const logout = async () => {
    try {
      await signOut();
      setUser(null);
    } catch (error) {
      console.error('Logout error:', error);
    }
  };

  const value = {
    user,
    loading,
    isAuthenticated: !!user,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useBetterAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useBetterAuth must be used within a BetterAuthProvider');
  }
  return context;
}