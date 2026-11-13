import { apiFetch } from './client'
import type { Task, TaskAssistance, TaskCreate, TaskUpdate } from '../types'

// listTasks() is implemented as an example. TODO: implement the others.
// Adjust the paths if your routes differ (e.g. trailing slash).

export async function listTasks(): Promise<Task[]> {
  // GET /v1/tasks
  return apiFetch<Task[]>('/v1/tasks/')
}

export async function createTask(data: TaskCreate): Promise<Task> {
  // POST /v1/tasks
  void data
  throw new Error('createTask() not implemented yet')
}

export async function updateTask(id: string, data: TaskUpdate): Promise<Task> {
  // PATCH /v1/tasks/{id}
  void id
  void data
  throw new Error('updateTask() not implemented yet')
}

export async function deleteTask(id: string): Promise<void> {
  // DELETE /v1/tasks/{id}
  void id
  throw new Error('deleteTask() not implemented yet')
}

export async function getTaskAssistance(id: string): Promise<TaskAssistance> {
  // POST /v1/tasks/{id}/assist
  void id
  throw new Error('getTaskAssistance() not implemented yet')
}
