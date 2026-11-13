"""
Task Assistant Agent (AI evaluates a task and helps the user execute it)
=========================================================================
A SECOND agent, different from the chat agent in app/agent/agent.py.
The chat agent *acts* (calls tools). This one *analyzes*: given one of the
user's tasks, it evaluates it and returns a structured action plan.

The main skill evaluated here is CONTEXT handling: deciding what
information the LLM needs, fetching it safely and sending it in a
clear, compact way.

You should implement here:

1. `AssistantDeps` dataclass with the context the agent needs, e.g.:
     - task: the task being analyzed (already loaded from the database)
     - related_tasks: a SHORT list of the user's other open tasks that may
       be relevant (e.g. same department) — limit it (e.g. max 5) and send
       only the fields that help (title, priority, status). Explain your
       choice in the README.

2. `task_assistant` agent:
     - model: settings.LLM_MODEL
     - deps_type: AssistantDeps
     - output_type: TaskAssistance (app/schemas/assistance.py) — the LLM
       output is validated by Pydantic; if it is invalid, PydanticAI asks
       the model to retry
     - instructions: TASK_ASSISTANT_PROMPT (app/agent/prompts.py)

3. Dynamic instructions that inject the context at run time:

       @task_assistant.instructions
       def task_context(ctx: RunContext[AssistantDeps]) -> str:
           return (
               f"Task title: {ctx.deps.task.title}\n"
               f"Description: {ctx.deps.task.description or 'not provided'}\n"
               ...
           )

Rules:
- The task MUST be loaded from the database filtered by the current user
  (never trust an id coming from the LLM or from another user).
- Do not send unnecessary or sensitive data to the LLM (e.g. password
  hashes, emails, other users' data, the whole task table).
- If the task has little information (e.g. no description), the agent
  should say so and return clarifying questions instead of inventing details.

Usage (in app/services/task_assistant_service.py):

    result = await task_assistant.run(
        "Evaluate this task and help me execute it.",
        deps=AssistantDeps(task=task, related_tasks=related),
    )
    result.output  # -> TaskAssistance

Docs:
- https://ai.pydantic.dev/output/          (structured output)
- https://ai.pydantic.dev/agents/#instructions
- https://ai.pydantic.dev/dependencies/
"""
