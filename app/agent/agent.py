"""
PydanticAI Agent Definition
============================
You should implement here:

- An `AgentDeps` dataclass holding what the tools need at runtime:
  the database session and the current user's id
- A PydanticAI `Agent` instance:
    * model: `settings.LLM_MODEL` (configurable via .env — "test" works
      without any API key, useful while developing)
    * deps_type: AgentDeps
    * instructions: SYSTEM_PROMPT (app/agent/prompts.py)
- Register the tools from app/agent/tools.py

Example (PydanticAI 2.x):

    from dataclasses import dataclass
    from uuid import UUID

    from pydantic_ai import Agent
    from sqlalchemy.ext.asyncio import AsyncSession

    from app.agent.prompts import SYSTEM_PROMPT
    from app.agent.tools import create_task_tool
    from app.config import settings


    @dataclass
    class AgentDeps:
        db: AsyncSession
        user_id: UUID


    agent = Agent(
        settings.LLM_MODEL,
        deps_type=AgentDeps,
        instructions=SYSTEM_PROMPT,
        tools=[create_task_tool],
    )

The agent is invoked by POST /v1/chat:

    result = await agent.run(message, deps=AgentDeps(db=db, user_id=user.id))
    result.output  # the agent's final answer

Docs: https://ai.pydantic.dev/agents/
"""
