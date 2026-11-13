"""
Task Assistance Schemas
========================
Structured output of the task assistant agent (app/agent/task_assistant.py)
and response model of `POST /v1/tasks/{task_id}/assist`.

You should implement here:
- TaskAssistance:
    summary (str)                  -> what the task is about, in 1-2 sentences
    complexity (low/medium/high)
    estimated_hours (float, > 0)   -> rough effort estimate
    suggested_priority (TaskPriority) + priority_reason (str)
                                   -> does the current priority make sense?
    steps (list[str], 1 to 7 items) -> concrete action plan, in order
    risks (list[str])              -> what could go wrong / attention points
    clarifying_questions (list[str]) -> what is missing to do the task well

Use `Field(...)` with constraints and `description=` on each field:
PydanticAI sends the schema (including descriptions) to the LLM, so good
descriptions improve the output, and the constraints reject bad output.

Example:
    class TaskAssistance(BaseModel):
        summary: str = Field(description="One or two sentences about the task")
        steps: list[str] = Field(min_length=1, max_length=7,
                                 description="Concrete, ordered steps")
        ...
"""
