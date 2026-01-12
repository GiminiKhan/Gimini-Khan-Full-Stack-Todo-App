import { signIn, signOut, useSession } from '@/lib/auth/client';

interface User {
  id: string;
  email: string;
  name?: string;
  emailVerified: boolean;
  image?: string;
}

// Better Auth wrapper functions
export const betterRegisterUser = async (userData: {
  email: string;
  password: string;
  name?: string;
}): Promise<User> => {
  try {
    // Use Better Auth's signUp method
    const response = await signIn.email({
      email: userData.email,
      password: userData.password,
      name: userData.name,
      redirectTo: '/dashboard', // Redirect after successful signup
    });

    return response.user;
  } catch (error) {
    console.error('Better Auth registration error:', error);
    throw error;
  }
};

export const betterLoginUser = async (credentials: {
  email: string;
  password: string;
}): Promise<{ user: User; token: string }> => {
  try {
    // Use Better Auth's signIn method
    const response = await signIn.email({
      email: credentials.email,
      password: credentials.password,
      redirectTo: '/dashboard', // Redirect after successful login
    });

    return {
      user: response.user,
      token: response.token || '', // Better Auth handles sessions automatically
    };
  } catch (error) {
    console.error('Better Auth login error:', error);
    throw error;
  }
};

export const betterCheckAuthStatus = async (): Promise<User | null> => {
  try {
    // Use the useSession hook to check authentication status
    // This is typically handled by the BetterAuthProvider context
    const response = await fetch('/api/auth/session'); // Better Auth session endpoint

    if (response.ok) {
      const sessionData = await response.json();
      return sessionData.user || null;
    }

    return null;
  } catch (error) {
    console.error('Better Auth status check error:', error);
    return null;
  }
};

export const betterLogoutUser = async (): Promise<void> => {
  try {
    await signOut({
      callbackURL: '/login', // Redirect after logout
    });
  } catch (error) {
    console.error('Better Auth logout error:', error);
    throw error;
  }
};

// OAuth sign-in functions
export const signInWithGoogle = async (): Promise<void> => {
  try {
    await signIn.social({
      provider: 'google',
      redirectTo: '/dashboard',
    });
  } catch (error) {
    console.error('Google sign-in error:', error);
    throw error;
  }
};

export const signInWithGitHub = async (): Promise<void> => {
  try {
    await signIn.social({
      provider: 'github',
      redirectTo: '/dashboard',
    });
  } catch (error) {
    console.error('GitHub sign-in error:', error);
    throw error;
  }
};