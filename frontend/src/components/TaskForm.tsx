import type { Task } from '../types'

interface TaskFormProps {
  onCreated: (task: Task) => void
}

/**
 * TODO: form to create a task.
 * - Fields: title, description (optional), priority (select), department
 * - Call createTask() on submit, then onCreated(task) and clear the form
 * - Show validation errors returned by the API (422)
 */
export default function TaskForm({ onCreated }: TaskFormProps) {
  void onCreated

  return (
    <section className="card">
      <h2>Nova tarefa</h2>
      <p className="muted">TODO: implementar formulário.</p>
    </section>
  )
}
