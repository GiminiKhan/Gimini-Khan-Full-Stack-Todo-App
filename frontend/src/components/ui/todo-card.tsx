'use client';

import { useState } from 'react';

interface TodoCardProps {
  todo: any;
  onUpdate: (id: string, updates: any) => void;
  onDelete: (id: string) => void;
}

export function TodoCard({ todo, onUpdate, onDelete }: TodoCardProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(todo.title);
  const [description, setDescription] = useState(todo.description || '');
  const [priority, setPriority] = useState(todo.priority);
  const [completed, setCompleted] = useState(todo.completed);

  const handleSave = () => {
    onUpdate(todo.id, { title, description, priority, completed });
    setIsEditing(false);
  };

  const handleCancel = () => {
    // Reset to original values
    setTitle(todo.title);
    setDescription(todo.description || '');
    setPriority(todo.priority);
    setCompleted(todo.completed);
    setIsEditing(false);
  };

  // Priority color mapping
  const priorityColors = {
    high: 'bg-red-100 text-red-800 border-red-200',
    medium: 'bg-amber-100 text-amber-800 border-amber-200',
    low: 'bg-blue-100 text-blue-800 border-blue-200',
  };

  const priorityText = {
    high: 'High',
    medium: 'Medium',
    low: 'Low',
  };

  return (
    <div className={`bg-white/80 backdrop-blur-md border border-white/20 rounded-2xl p-4 shadow-sm transition-all duration-300 hover:shadow-md ${completed ? 'bg-green-50/80' : 'bg-white/80'}`}>
      {isEditing ? (
        <div className="space-y-3">
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full p-2 border border-slate-300 rounded-lg bg-white/70"
            placeholder="Title"
          />
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full p-2 border border-slate-300 rounded-lg bg-white/70"
            placeholder="Description"
          />
          <select
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
            className="w-full p-2 border border-slate-300 rounded-lg bg-white/70"
          >
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
          <div className="flex items-center">
            <input
              type="checkbox"
              id={`completed-${todo.id}`}
              checked={completed}
              onChange={(e) => setCompleted(e.target.checked)}
              className="mr-2 h-4 w-4 text-indigo-600 rounded focus:ring-indigo-500"
            />
            <label htmlFor={`completed-${todo.id}`} className="text-sm text-slate-700">
              Completed
            </label>
          </div>
          <div className="flex space-x-2">
            <button
              onClick={handleSave}
              className="flex-1 bg-indigo-600 text-white py-2 px-3 rounded-lg hover:bg-indigo-700 transition-colors"
            >
              Save
            </button>
            <button
              onClick={handleCancel}
              className="flex-1 bg-slate-500 text-white py-2 px-3 rounded-lg hover:bg-slate-600 transition-colors"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <>
          <div className="flex justify-between items-start mb-3">
            <h3 className={`font-semibold text-slate-800 ${completed ? 'line-through' : ''}`}>{todo.title}</h3>
            <span className={`text-xs px-2.5 py-0.5 rounded-full font-medium ${priorityColors[priority as keyof typeof priorityColors]}`}>
              {priorityText[priority as keyof typeof priorityText]}
            </span>
          </div>
          {todo.description && (
            <p className={`text-sm mb-3 text-slate-600 ${completed ? 'line-through' : ''}`}>{todo.description}</p>
          )}
          <div className="flex items-center justify-between pt-3 border-t border-white/20">
            <div className="flex items-center">
              <input
                type="checkbox"
                id={`toggle-${todo.id}`}
                checked={completed}
                onChange={(e) => setCompleted(e.target.checked)}
                className="mr-2 h-4 w-4 text-indigo-600 rounded focus:ring-indigo-500"
              />
              <label htmlFor={`toggle-${todo.id}`} className="text-sm text-slate-600">
                {completed ? 'Completed' : 'Mark Complete'}
              </label>
            </div>
            <div className="flex space-x-3">
              <button
                onClick={() => setIsEditing(true)}
                className="text-indigo-600 hover:text-indigo-800 text-sm font-medium transition-colors"
              >
                Edit
              </button>
              <button
                onClick={() => onDelete(todo.id)}
                className="text-red-600 hover:text-red-800 text-sm font-medium transition-colors"
              >
                Delete
              </button>
            </div>
          </div>
        </>
      )}
    </div>
  );
}