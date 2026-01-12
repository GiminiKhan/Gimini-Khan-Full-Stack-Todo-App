import { signIn, signOut, useSession } from '@/lib/auth/client';

interface User {
  id: string;
  email: string;
  full_name?: string;
  emailVerified?: boolean;
  image?: string | null;
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

// Register a new user using Better Auth
export const registerUser = async (userData: RegisterData): Promise<User> => {
  console.log('Attempting registration with data:', userData);
  try {
    // Use Better Auth's sign up method
    const response = await signIn.email({
      email: userData.email,
      password: userData.password,
      callbackURL: '/dashboard', // Redirect after successful signup
    });

    console.log('Registration response received:', response);

    // Return a user object compatible with our interface
    return {
      id: response.data?.user?.id || '',
      email: response.data?.user?.email || '',
      full_name: response.data?.user?.name,
      is_active: true,
    };
  } catch (error) {
    console.error('Better Auth registration error:', error);
    throw error;
  }
};

// Login user using Better Auth
export const loginUser = async (credentials: LoginCredentials): Promise<AuthResponse> => {
  console.log('Attempting login with credentials:', credentials);
  try {
    // Use Better Auth's sign in method
    const response = await signIn.email({
      email: credentials.email,
      password: credentials.password,
      callbackURL: '/dashboard', // Redirect after successful login
    });

    console.log('Login response received:', response);

    // For compatibility with existing code, return a token-like response
    // In Better Auth, the session is typically handled via cookies
    return {
      access_token: response.data?.token || 'better_auth_session', // Better Auth handles sessions automatically
      token_type: 'bearer',
    };
  } catch (error) {
    console.error('Better Auth login error:', error);
    throw error;
  }
};

// Check if user is authenticated using Better Auth
export const checkAuthStatus = async (): Promise<User | null> => {
  console.log('Checking auth status...');
  try {
    // In Better Auth, session status is typically checked via the useSession hook
    // For this function, we'll return the current session if available
    // Note: This would normally be handled by the BetterAuthProvider context
    const response = await fetch('/api/auth/session'); // Better Auth session endpoint
    console.log('Auth status response:', response.status);

    if (response.ok) {
      const sessionData = await response.json();
      console.log('Session data:', sessionData);
      if (sessionData.user) {
        return {
          id: sessionData.user.id,
          email: sessionData.user.email,
          full_name: sessionData.user.name || sessionData.user.email.split('@')[0],
          is_active: true,
        };
      }
    }

    return null;
  } catch (error) {
    console.error('Better Auth status check error:', error);
    return null;
  }
};

// Logout user using Better Auth
export const logoutUser = async (): Promise<void> => {
  try {
    await signOut(); // Better Auth handles logout
  } catch (error) {
    console.error('Better Auth logout error:', error);
    throw error;
  }
};

// Save Better Auth session token to localStorage (if needed for API calls)
export const saveAccessToken = (token: string): void => {
  localStorage.setItem('better-auth.session_token', token);
};

// Get Better Auth session token from localStorage
export const getAccessToken = (): string | null => {
  return localStorage.getItem('better-auth.session_token');
};

// Sign in with OAuth providers
export const signInWithGoogle = async (callbackURL: string = '/dashboard'): Promise<void> => {
  try {
    await signIn.social({
      provider: 'google',
      callbackURL: callbackURL,
    });
  } catch (error) {
    console.error('Google sign-in error:', error);
    throw error;
  }
};

export const signInWithGitHub = async (callbackURL: string = '/dashboard'): Promise<void> => {
  try {
    await signIn.social({
      provider: 'github',
      callbackURL: callbackURL,
    });
  } catch (error) {
    console.error('GitHub sign-in error:', error);
    throw error;
  }
};