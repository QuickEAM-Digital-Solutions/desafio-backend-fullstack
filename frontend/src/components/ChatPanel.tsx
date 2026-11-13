import type { Task } from '../types'

interface ChatPanelProps {
  onTaskCreated: (task: Task) => void
}

/**
 * TODO: chat with the AI agent.
 * - Keep the conversation history in state (user messages + agent replies)
 * - Send the message with sendChatMessage() and show a "pensando..." state
 * - Show the agent's reply
 * - If the response contains created_task, call onTaskCreated(task)
 * - Handle errors (e.g. LLM unavailable) with a friendly message
 */
export default function ChatPanel({ onTaskCreated }: ChatPanelProps) {
  void onTaskCreated

  return (
    <aside className="card">
      <h2>Assistente IA</h2>
      <p className="muted">
        Ex.: “Cadastre uma tarefa urgente chamada ‘Revisar relatório financeiro’ para o
        departamento Comercial”
      </p>
      <p className="muted">TODO: implementar chat.</p>
    </aside>
  )
}
