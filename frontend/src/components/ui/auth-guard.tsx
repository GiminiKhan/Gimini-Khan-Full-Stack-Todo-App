'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { authService } from '../../services/auth-client';

interface AuthGuardProps {
  children: React.ReactNode;
  requireAuth?: boolean; // If true, requires authentication; if false, redirects away if authenticated
}

export function AuthGuard({ children, requireAuth = true }: AuthGuardProps) {
  const router = useRouter();

  useEffect(() => {
    const checkAuth = async () => {
      const isAuthenticated = authService.isAuthenticated();

      if (requireAuth && !isAuthenticated) {
        // Redirect to login if authentication is required but user is not logged in
        router.push('/auth/login');
      } else if (!requireAuth && isAuthenticated) {
        // Redirect away if user is logged in but shouldn't be (e.g., login page)
        router.push('/dashboard');
      }
    };

    checkAuth();
  }, [requireAuth, router]);

  // For now, just return the children - the redirect will happen in useEffect
  return <>{children}</>;
}