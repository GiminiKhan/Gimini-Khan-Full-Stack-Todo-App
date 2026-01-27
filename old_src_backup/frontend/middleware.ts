import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export default async function middleware(request: NextRequest) {
  // For now, allow all requests to pass through
  // In a real implementation, you would verify the Better Auth session token from cookies
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*', '/api/auth/:path*']
};