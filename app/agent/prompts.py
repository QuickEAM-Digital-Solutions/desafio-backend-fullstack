"""
AI Agent System Prompt
=======================
You should implement here:

- SYSTEM_PROMPT: clear instructions for the LLM.

A good prompt should:
1. Define the agent's role (task management assistant)
2. Explain when to use each tool
3. Explain how to map natural language to fields
   (e.g. "urgente" -> priority "urgent", "para o Comercial" -> department "Comercial")
4. Say what to do when information is missing (ask the user, don't invent)
5. Define the language/tone of the answer (e.g. answer in the user's language)

Example:
    SYSTEM_PROMPT = '''
    You are a task management assistant.
    When the user asks to create a task, call `create_task_tool`.
    Priority must be one of: low, medium, high, urgent.
    If the title or department is missing, ask the user before creating.
    Answer in the same language the user wrote in.
    '''

-------------------------------------------------------------------------

- TASK_ASSISTANT_PROMPT: instructions for the task assistant agent
  (app/agent/task_assistant.py).

A good prompt should:
1. Define the role (a pragmatic assistant that helps the user execute a task)
2. Explain what to evaluate: complexity, effort, whether the priority
   makes sense, missing information
3. Ask for concrete, actionable steps (not generic advice)
4. Tell the model to rely ONLY on the provided context and to ask
   clarifying questions when information is missing
5. Define the language of the answer (e.g. Portuguese, or the task's language)

Note: the task data is NOT written here — it is injected at run time via
dynamic instructions (`@task_assistant.instructions`). Keep the static
prompt and the dynamic context separate.
"""
