"""
Task Service (Business Logic)
==============================
You should implement here (all functions async, all scoped by user_id):

- create_task(db, user_id, data: TaskCreate) -> Task
- list_tasks(db, user_id, status=None, priority=None, skip=0, limit=20) -> list[Task]
- get_task(db, user_id, task_id) -> Task   (raise a "not found" error if missing
  or owned by another user)
- update_task(db, user_id, task_id, data: TaskUpdate) -> Task
- delete_task(db, user_id, task_id) -> None

This service is called by:
- Task CRUD endpoints (app/api/v1/endpoints/tasks.py)
- AI agent tools (app/agent/tools.py)

Keeping the logic here means the API and the agent share the same rules.
"""
