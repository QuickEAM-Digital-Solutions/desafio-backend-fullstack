"""
AI Chat Endpoint
================
You should implement here:

- POST /v1/chat: receives the user's message, runs the PydanticAI agent
  (app/agent/agent.py) and returns its response.

The endpoint must:
1. Require authentication (`Depends(get_current_user)`)
2. Build the agent dependencies (db session + current user id) and call
   `await agent.run(message, deps=...)`
3. Return a `ChatResponse` (app/schemas/chat.py)
4. Handle LLM failures gracefully: if the model/provider fails, return a
   clear error (e.g. 502/503) instead of an unhandled 500 with a stack trace.

Example request body:
    {
        "message": "Cadastre uma tarefa urgente chamada 'Revisar relatório
                    financeiro' para o departamento Comercial"
    }

Expected result: a new task (priority=urgent, department=Comercial) exists in
the database for the CURRENT user, and the response explains what was done.
"""

from fastapi import APIRouter

router = APIRouter()
