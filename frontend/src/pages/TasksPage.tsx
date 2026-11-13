import ChatPanel from '../components/ChatPanel'
import TaskAssistantPanel from '../components/TaskAssistantPanel'
import TaskForm from '../components/TaskForm'
import TaskList from '../components/TaskList'
import type { Task } from '../types'

interface TasksPageProps {
  onLogout: () => void
}

/**
 * Main page: task list + creation form + AI chat.
 *
 * TODO:
 * - Load the user's tasks from the API when the page opens (listTasks)
 * - Keep the tasks in state and handle loading / error states
 * - Refresh (or update) the list when:
 *     * a task is created through the form
 *     * a task is updated/deleted in the list
 *     * the AI chat creates a task (ChatResponse.created_task)
 * - If the API returns 401 (expired token), log the user out
 * - Keep the task selected for AI help in state and show TaskAssistantPanel
 */
export default function TasksPage({ onLogout }: TasksPageProps) {
  const tasks: Task[] = []
  const assistedTask: Task | null = null

  return (
    <main className="container">
      <header className="row between">
        <h1>Minhas tarefas</h1>
        <button onClick={onLogout}>Sair</button>
      </header>

      <div className="grid">
        <section className="stack">
          <TaskForm onCreated={() => {}} />
          <TaskList tasks={tasks} onChanged={() => {}} onAssist={() => {}} />
        </section>

        <ChatPanel onTaskCreated={() => {}} />
      </div>

      {assistedTask && <TaskAssistantPanel task={assistedTask} onClose={() => {}} />}
    </main>
  )
}
