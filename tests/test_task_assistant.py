"""
Task Assistant Tests
=====================
Use PydanticAI's `TestModel` — tests must NOT call a real LLM.
`TestModel` automatically generates an output that matches your
`TaskAssistance` schema.

You should implement here:
- test_assist_returns_structured_plan: POST /v1/tasks/{id}/assist returns
  200 with summary, complexity, steps, etc.
- test_assist_other_user_task_returns_404: a user cannot ask for help on
  another user's task
- test_assist_context_contains_task_data: the task data reaches the LLM.
  Tip: capture the messages sent to the model with `capture_run_messages`
  (from pydantic_ai import capture_run_messages) or `FunctionModel`, and
  assert the task title is in the instructions — and that data from other
  users is NOT
- test_assist_handles_llm_failure: returns a controlled error (e.g. 503)

Docs: https://ai.pydantic.dev/testing/
"""
