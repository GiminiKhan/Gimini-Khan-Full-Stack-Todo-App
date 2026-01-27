import { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';

export async function GET(request: NextRequest, { params }: { params: { slug: string[] } }) {
  // Extract the auth action from the slug (e.g., ['session'], ['sign-in'], etc.)
  const action = params.slug?.join('/') || '';

  // Proxy the request to the backend auth service
  const backendUrl = `${process.env.BACKEND_URL || 'http://localhost:8000'}/api/auth/${action}`;

  // Clone headers, removing Next.js-specific ones that shouldn't be forwarded
  const headers = new Headers();
  request.headers.forEach((value, key) => {
    // Skip headers that shouldn't be forwarded to the backend
    if (!['content-length', 'host'].includes(key.toLowerCase())) {
      headers.set(key, value);
    }
  });

  const response = await fetch(backendUrl, {
    method: 'GET',
    headers,
  });

  // Create response with body and proper headers
  const responseBody = await response.text();
  return new NextResponse(responseBody, {
    status: response.status,
    headers: response.headers,
  });
}

export async function POST(request: NextRequest, { params }: { params: { slug: string[] } }) {
  // Extract the auth action from the slug
  const action = params.slug?.join('/') || '';

  // Get the request body
  const body = await request.text();

  // Proxy the request to the backend auth service
  const backendUrl = `${process.env.BACKEND_URL || 'http://localhost:8000'}/api/auth/${action}`;

  // Clone headers, removing Next.js-specific ones that shouldn't be forwarded
  const headers = new Headers();
  request.headers.forEach((value, key) => {
    // Skip headers that shouldn't be forwarded to the backend
    if (!['content-length', 'host'].includes(key.toLowerCase())) {
      headers.set(key, value);
    }
  });
  headers.set('Content-Type', 'application/json');

  const response = await fetch(backendUrl, {
    method: 'POST',
    headers,
    body,
  });

  // Create response with body and proper headers
  const responseBody = await response.text();
  return new NextResponse(responseBody, {
    status: response.status,
    headers: response.headers,
  });
}