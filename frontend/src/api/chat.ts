import type { ChatResponse } from '../types'

/**
 * TODO: call POST /v1/chat with { message } using apiFetch().
 */
export async function sendChatMessage(message: string): Promise<ChatResponse> {
  void message
  throw new Error('sendChatMessage() not implemented yet')
}
