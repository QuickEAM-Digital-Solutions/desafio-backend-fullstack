"""
AI Chat Endpoint Tests
=======================
Use PydanticAI's `TestModel` (see tests/conftest.py) — tests must NOT call
a real LLM API.

You should implement here:
- test_chat_requires_auth: unauthenticated request returns 401
- test_chat_creates_task: after a chat message, a task exists in the database
  for the CURRENT user (TestModel calls your tools automatically)
- test_chat_handles_llm_failure: when the model raises an error, the endpoint
  returns a controlled error response instead of crashing
  (tip: `FunctionModel` from `pydantic_ai.models.function` lets you simulate it)
"""
