"""
Task Assistant Service
=======================
Builds the context and runs the task assistant agent.

You should implement here:
- assist_task(db, user_id, task_id) -> TaskAssistance
    1. Load the task with task_service.get_task(db, user_id, task_id)
       (raises "not found" if it doesn't exist or belongs to another user)
    2. Load a small list of related open tasks of the SAME user
       (e.g. same department, not completed, max 5)
    3. Run `task_assistant` with AssistantDeps(task=..., related_tasks=...)
    4. Return result.output
    5. Log the call (task_id, duration, success/failure) — never log the
       full prompt with user data at INFO level

Error handling: if the LLM provider fails or the output can't be validated
after retries, raise an application error that the route converts into a
controlled HTTP error (e.g. 503).

(Optional/diferencial) Cache the result so the same task is not sent to
the LLM again until it changes (e.g. store it in a JSON column together
with the task's updated_at, or use Redis).
"""
