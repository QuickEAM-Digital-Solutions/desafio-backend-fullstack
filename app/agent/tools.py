"""
AI Agent Tools (Tool Calling)
==============================
Functions the PydanticAI agent can call autonomously.

Required:
- create_task_tool: receives the entities extracted by the LLM (title,
  priority, department, optional description), validates them with the
  `TaskCreate` schema and saves the task via `task_service.create_task`
  for the CURRENT user (`ctx.deps.user_id`).

Optional (diferencial):
- list_tasks_tool: lets the user ask "quais são minhas tarefas urgentes?"

Each tool must:
1. Have typed parameters and a clear docstring (PydanticAI sends the
   docstring and the parameter types to the LLM as the tool description)
2. Get the db session and user id from `ctx.deps` — NEVER from the LLM
3. Return a small structured result (dict or Pydantic model)

Example:
    from pydantic_ai import RunContext

    async def create_task_tool(
        ctx: RunContext["AgentDeps"],
        title: str,
        priority: TaskPriority,
        department: str,
        description: str | None = None,
    ) -> dict:
        \"\"\"Create a new task for the current user.\"\"\"
        data = TaskCreate(title=title, priority=priority, department=department,
                          description=description)
        task = await task_service.create_task(ctx.deps.db, ctx.deps.user_id, data)
        return {"task_id": str(task.id), "title": task.title}

Docs: https://ai.pydantic.dev/tools/
"""
