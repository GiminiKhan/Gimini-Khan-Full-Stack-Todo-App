'use client';

interface SkeletonLoaderProps {
  className?: string;
}

export function SkeletonLoader({ className = '' }: SkeletonLoaderProps) {
  return (
    <div
      className={`animate-pulse bg-slate-200 rounded-md ${className}`}
      style={{ animationDuration: '1.5s' }}
    />
  );
}

interface SkeletonCardProps {
  count?: number;
}

export function SkeletonCard({ count = 1 }: SkeletonCardProps) {
  return (
    <>
      {[...Array(count)].map((_, idx) => (
        <div key={idx} className="border rounded-2xl p-4 shadow-sm bg-white/50 backdrop-blur-sm">
          <SkeletonLoader className="h-5 w-3/4 mb-3" />
          <SkeletonLoader className="h-4 w-full mb-2" />
          <SkeletonLoader className="h-4 w-2/3 mb-4" />
          <div className="flex justify-between">
            <SkeletonLoader className="h-6 w-16 rounded-full" />
            <SkeletonLoader className="h-8 w-20 rounded-md" />
          </div>
        </div>
      ))}
    </>
  );
}