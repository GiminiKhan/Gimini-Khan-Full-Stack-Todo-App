'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    // Redirect to login page immediately
    router.push('/login');
  }, [router]);

  // Show a minimal loading state while redirecting
  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="text-lg">Redirecting to login...</div>
    </div>
  );
}