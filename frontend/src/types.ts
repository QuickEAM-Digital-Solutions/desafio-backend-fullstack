// Types mirroring the backend Pydantic schemas.
// Keep them in sync with app/schemas/*.py (adjust if your API differs).

export type TaskStatus = 'pending' | 'in_progress' | 'completed'
export type TaskPriority = 'low' | 'medium' | 'high' | 'urgent'

export interface Task {
  id: string
  title: string
  description: string | null
  status: TaskStatus
  priority: TaskPriority
  department: string
  created_at: string
  updated_at: string
}

export interface TaskCreate {
  title: string
  description?: string | null
  priority: TaskPriority
  department: string
}

export type TaskUpdate = Partial<TaskCreate & { status: TaskStatus }>

export interface ChatResponse {
  reply: string
  created_task: Task | null
}

export interface TokenResponse {
  access_token: string
  token_type: string
}

export interface TaskAssistance {
  summary: string
  complexity: 'low' | 'medium' | 'high'
  estimated_hours: number
  suggested_priority: TaskPriority
  priority_reason: string
  steps: string[]
  risks: string[]
  clarifying_questions: string[]
}
