import type { Task } from '../types'

interface TaskListProps {
  tasks: Task[]
  onChanged: () => void
  onAssist: (task: Task) => void
}

/**
 * TODO: render the user's tasks.
 * - Show title, priority, status and department
 * - Allow changing the status (e.g. a select or a "concluir" button) -> updateTask()
 * - Allow deleting a task -> deleteTask()
 * - Call onChanged() after any change so the page can refresh the list
 * - A "Pedir ajuda à IA" button on each task -> onAssist(task)
 * - Show an empty state when there are no tasks
 * - (Optional) filters by status/priority
 */
export default function TaskList({ tasks, onChanged, onAssist }: TaskListProps) {
  void onChanged
  void onAssist

  return (
    <section className="card">
      <h2>Tarefas ({tasks.length})</h2>
      <p className="muted">TODO: implementar listagem.</p>
    </section>
  )
}
