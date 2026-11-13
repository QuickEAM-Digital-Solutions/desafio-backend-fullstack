"""
Task Schemas
=============
Pydantic v2 models for task CRUD and for the AI agent tool validation.

You should implement here:
- TaskStatus and TaskPriority enums (reuse them in the SQLAlchemy model)
- TaskCreate: title (str, 3-200 chars), description (str | None),
  priority (TaskPriority, default medium), department (str)
- TaskUpdate: all fields optional (for PATCH), including status
- TaskResponse: all fields + id, status, created_at, updated_at
  (`from_attributes=True`)
- (Optional) TaskListResponse: items + pagination metadata (total, skip, limit)

`TaskCreate` is also used by the AI agent tool: the data extracted by the
LLM must pass through it before reaching the database.
"""
