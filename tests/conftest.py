"""
Test Configuration & Fixtures
==============================
`async_client` is ready to use. Implement the remaining fixtures.

You should implement here:
- A test database strategy. Suggestions (pick one and explain it in the README):
    a) a separate Postgres database (e.g. TEST_DATABASE_URL) whose tables are
       created/dropped with `Base.metadata.create_all/drop_all`
    b) one transaction per test, rolled back at the end
  Then override the `get_db` dependency so the app uses the test session:
      app.dependency_overrides[get_db] = override_get_db
- user / other_user: fixtures that create users in the test database
- auth_headers: {"Authorization": f"Bearer {token}"} for `user`

Testing the AI agent WITHOUT calling a real LLM:
PydanticAI ships `TestModel`, a fake model that calls your tools with
generated arguments and never hits the network. Example:

    from pydantic_ai.models.test import TestModel
    from app.agent.agent import agent

    async def test_chat_creates_task(async_client, auth_headers):
        with agent.override(model=TestModel()):
            response = await async_client.post(
                "/v1/chat", json={"message": "Crie uma tarefa..."}, headers=auth_headers
            )
        assert response.status_code == 200

Docs: https://ai.pydantic.dev/testing/
"""

from collections.abc import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """HTTP client that calls the FastAPI app in-process (no server needed)."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
