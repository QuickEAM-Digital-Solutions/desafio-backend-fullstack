import type { Task } from '../types'

interface TaskAssistantPanelProps {
  task: Task
  onClose: () => void
}

/**
 * TODO: show the AI evaluation of a task and the plan to execute it.
 * - Call getTaskAssistance(task.id) when the panel opens (or when task changes)
 * - Show a loading state: the LLM may take a few seconds
 * - Render the TaskAssistance fields: summary, complexity, estimated hours,
 *   suggested priority (+ reason), ordered steps, risks and clarifying questions
 * - Handle errors (e.g. 503 when the LLM is unavailable) with a friendly message
 * - (Optional) a "Gerar novamente" button and checkboxes to mark steps as done
 *
 * It can be a modal, a drawer or an inline section — your choice.
 */
export default function TaskAssistantPanel({ task, onClose }: TaskAssistantPanelProps) {
  return (
    <section className="card">
      <header className="row between">
        <h2>Ajuda da IA: {task.title}</h2>
        <button onClick={onClose}>Fechar</button>
      </header>
      <p className="muted">TODO: implementar avaliação e plano de execução.</p>
    </section>
  )
}
