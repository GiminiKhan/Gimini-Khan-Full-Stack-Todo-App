'use client';

import { useAuth } from '@/context/AuthContext';
import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { getTasks, createTask, deleteTask, toggleTaskCompletion } from '@/services/todo';
import { Task, CreateTaskData } from '@/types/todo';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Checkbox } from '@/components/ui/checkbox';
import { Label } from '@/components/ui/label';
import { useToast } from '@/hooks/use-toast';
import { Trash2, Plus } from 'lucide-react';

export default function DashboardPage() {
  const { user, loading: authLoading, logout } = useAuth();
  const router = useRouter();
  const { toast } = useToast();
  const [mounted, setMounted] = useState(false);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [formLoading, setFormLoading] = useState(false);
  const [newTask, setNewTask] = useState<CreateTaskData>({ title: '', description: '' });

  useEffect(() => {
    setMounted(true);
    // Check if user is authenticated
    console.log("Current User:", user);
    console.log("Auth Loading:", authLoading);
    // Temporary bypass for testing - commenting out redirect
    // if (!authLoading && !user) {
    //   // Redirect to login if not authenticated
    //   router.push('/login');
    // }
  }, [user, authLoading, router]);

  useEffect(() => {
    if (user && mounted) {
      fetchTasks();
    } else if (!authLoading && !user) {
      console.log("No user authenticated, staying on dashboard for testing");
    }
  }, [user, mounted, authLoading]);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const tasksData = await getTasks();
      setTasks(tasksData);
    } catch (error) {
      console.error('Error fetching tasks:', error);
      toast({
        title: 'Error',
        description: 'Failed to load tasks. Please try again.',
        variant: 'destructive',
      });
    } finally {
      setLoading(false);
    }
  };

  const handleCreateTask = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTask.title.trim()) return;

    setFormLoading(true);
    try {
      const taskToCreate = {
        ...newTask,
        is_completed: false, // Default to false
      };
      const createdTask = await createTask(taskToCreate);
      setTasks([createdTask, ...tasks]);
      setNewTask({ title: '', description: '' });

      toast({
        title: 'Task Created',
        description: 'Your task has been created successfully!',
      });
    } catch (error) {
      console.error('Error creating task:', error);
      toast({
        title: 'Error',
        description: 'Failed to create task. Please try again.',
        variant: 'destructive',
      });
    } finally {
      setFormLoading(false);
    }
  };

  const handleToggleTask = async (id: string, isCompleted: boolean) => {
    try {
      const updatedTask = await toggleTaskCompletion(id, !isCompleted);
      setTasks(tasks.map(task => task.id === id ? updatedTask : task));
    } catch (error) {
      console.error('Error toggling task:', error);
      toast({
        title: 'Error',
        description: 'Failed to update task. Please try again.',
        variant: 'destructive',
      });
    }
  };

  const handleDeleteTask = async (id: string) => {
    try {
      await deleteTask(id);
      setTasks(tasks.filter(task => task.id !== id));

      toast({
        title: 'Task Deleted',
        description: 'Your task has been deleted successfully!',
      });
    } catch (error) {
      console.error('Error deleting task:', error);
      toast({
        title: 'Error',
        description: 'Failed to delete task. Please try again.',
        variant: 'destructive',
      });
    }
  };

  if (authLoading || !mounted) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-lg">Loading...</div>
      </div>
    );
  }

  // For testing purposes, render the dashboard even if not authenticated
  // if (!user) {
  //   return null; // Will redirect in useEffect
  // }

  return (
    <div className="container mx-auto py-10">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">Todo Dashboard</h1>

        {/* Add Task Form */}
        <Card className="mb-8">
          <CardHeader>
            <CardTitle>Add New Task</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleCreateTask} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="title">Title</Label>
                <Input
                  id="title"
                  value={newTask.title}
                  onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
                  placeholder="What needs to be done?"
                  required
                />
              </div>
              <div className="space-y-2">
                <Label htmlFor="description">Description</Label>
                <Textarea
                  id="description"
                  value={newTask.description}
                  onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => setNewTask({ ...newTask, description: e.target.value })}
                  placeholder="Add details (optional)"
                />
              </div>
              <Button type="submit" disabled={formLoading} className="w-full">
                {formLoading ? (
                  <span className="flex items-center">
                    <span className="mr-2">Creating...</span>
                    <span className="animate-spin">⏳</span>
                  </span>
                ) : (
                  <span className="flex items-center">
                    <Plus className="mr-2 h-4 w-4" />
                    Add Task
                  </span>
                )}
              </Button>
            </form>
          </CardContent>
        </Card>

        {/* Tasks List */}
        <div className="space-y-4">
          <h2 className="text-2xl font-semibold">Your Tasks</h2>

          {loading ? (
            <div className="text-center py-8">Loading tasks...</div>
          ) : tasks.length === 0 ? (
            <div className="text-center py-12">
              <p className="text-lg text-gray-500">No tasks yet. Add your first task above!</p>
            </div>
          ) : (
            <div className="space-y-3">
              {tasks.map((task) => (
                <Card key={task.id} className="flex items-center justify-between p-4">
                  <div className="flex items-center space-x-3">
                    <Checkbox
                      id={`task-${task.id}`}
                      checked={task.is_completed}
                      onCheckedChange={() => handleToggleTask(task.id, task.is_completed)}
                    />
                    <div>
                      <Label
                        htmlFor={`task-${task.id}`}
                        className={`text-base ${task.is_completed ? 'line-through text-gray-500' : ''}`}
                      >
                        {task.title}
                      </Label>
                      {task.description && (
                        <p className={`text-sm ${task.is_completed ? 'text-gray-500' : 'text-gray-600'}`}>
                          {task.description}
                        </p>
                      )}
                    </div>
                  </div>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => handleDeleteTask(task.id)}
                    className="text-red-500 hover:text-red-700"
                  >
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </Card>
              ))}
            </div>
          )}
        </div>

        {/* Logout Button */}
        <div className="mt-8 flex justify-end">
          <Button
            variant="outline"
            onClick={() => {
              logout();
              router.push('/login');
            }}
          >
            Logout
          </Button>
        </div>
      </div>
    </div>
  );
}