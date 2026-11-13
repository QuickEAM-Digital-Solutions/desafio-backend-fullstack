"""
Chat Schemas
============
Pydantic v2 models for the AI chat endpoint.

You should implement here:
- ChatRequest: message (str, not empty, reasonable max length)
- ChatResponse: reply (str) - the agent's text answer,
  created_task (TaskResponse | None) - the task created by the agent, if any

The frontend uses `created_task` to refresh the task list after a chat message.
"""
