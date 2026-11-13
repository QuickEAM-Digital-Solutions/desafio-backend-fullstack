"""
Task CRUD Endpoints
====================
You should implement here:

- GET    /v1/tasks         -> list the current user's tasks
                              (optional filters: status, priority; pagination)
- POST   /v1/tasks         -> create a task owned by the current user
- GET    /v1/tasks/{id}    -> get one task
- PATCH  /v1/tasks/{id}    -> partially update a task
- DELETE /v1/tasks/{id}    -> delete a task (204 No Content)
- POST   /v1/tasks/{id}/assist -> the AI evaluates the task and returns an
                              action plan (`TaskAssistance`). Uses
                              app/services/task_assistant_service.py.
                              Same isolation rule: 404 for other users' tasks.

All routes must:
1. Require authentication (`Depends(get_current_user)`)
2. Only operate on tasks owned by the current user. Accessing a task that
   belongs to another user must return 404 (do not reveal it exists).
3. Use Pydantic schemas for request bodies and `response_model`.
4. Keep the route thin: business logic goes in app/services/task_service.py.
"""

from fastapi import APIRouter

router = APIRouter()
