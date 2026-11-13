# Technical Challenge — Junior FullStack Developer (Backend Focus · Python / AI)

> 🇧🇷 Versão em português: [README.md](README.md)

## Objective

You will build a **task manager with an AI assistant**: each user logs in, manages their own tasks through a React interface, can ask an AI agent, in natural language, to create tasks for them, and can ask the AI to **evaluate a task and build a plan to execute it**.

The focus is the **backend**. We want to evaluate your ability to build a clean, validated and well-organized API, and to integrate an AI agent into a real product flow. The frontend is simpler and is there to show you can consume your own API.

We don't expect a perfect system. We prefer **simple, readable, well-explained code** over many half-finished features. If you can't finish something, write in the README what is missing and how you would do it.

## Tech Stack

| Layer | Technologies |
|---|---|
| Language | Python 3.11+ (`async`/`await` and type hints) |
| Web Framework | FastAPI (async routes, `Depends`, automatic Swagger) |
| Validation | Pydantic v2 |
| AI | PydanticAI (agent + tool calling) |
| Database | PostgreSQL + SQLAlchemy 2.0 (async) + Alembic |
| Frontend | React + TypeScript (Vite). **Next.js is also accepted** |
| Infra | Docker and Docker Compose |
| Standards | PEP8 (ruff), code and logs in English, standardized commits |

## What is already provided

So you can focus on what matters, the repository already includes:

- ✅ **Docker Compose** with the API, PostgreSQL and the frontend (`docker compose up --build`)
- ✅ Typed **settings** with `pydantic-settings` ([app/config.py](app/config.py))
- ✅ **Async database connection** ([app/core/database.py](app/core/database.py)) and the `get_db()` dependency ([app/api/deps.py](app/api/deps.py))
- ✅ **Security helpers**: password hashing (bcrypt) and JWT creation/validation ([app/core/security.py](app/core/security.py))
- ✅ A ready **`User` model** to use as a reference ([app/models/user.py](app/models/user.py))
- ✅ **Alembic** configured and the v1 **router** already registered
- ✅ A **test HTTP client** (`async_client`) and an example test ([tests/](tests/))
- ✅ A **frontend skeleton** in React + TypeScript that already builds, with an HTTP client, pages and components ([frontend/](frontend/))

Every file you need to complete has a header comment saying **"You should implement here"** that explains what is expected.

## Challenge Scope

### Part 1: Authentication and Task CRUD (required)

1. **JWT authentication**
   - `POST /v1/auth/register`: creates a user (password stored hashed).
   - `POST /v1/auth/login`: validates credentials and returns a JWT.
   - `GET /v1/auth/me`: returns the authenticated user.
   - Implement the `get_current_user()` dependency in [app/api/deps.py](app/api/deps.py).

2. **Task CRUD** (`/v1/tasks`)
   - Create, list, get by ID, partially update (`PATCH`) and delete.
   - Fields: `title`, `description`, `status` (`pending` / `in_progress` / `completed`), `priority` (`low` / `medium` / `high` / `urgent`), `department`, `created_at` and `updated_at`.
   - Validation with **Pydantic v2 schemas** and `response_model` on the routes.

3. **Per-user isolation** 🔒
   - Each task belongs to one user (`user_id`).
   - A user must **never** see, change or delete another user's tasks. Accessing another user's task must return `404`.

4. **Database**
   - A `Task` model with SQLAlchemy 2.0 (`Mapped[...]` style).
   - At least **one Alembic migration** creating the tables.

### Part 2: AI Agent with PydanticAI (required)

1. **`POST /v1/chat` endpoint** (authenticated): receives the user's message and returns the agent's answer.
2. A **PydanticAI agent** with a clear system prompt ([app/agent/](app/agent/)).
3. A **`create_task` tool**: the agent extracts the information from the message, validates it with the Pydantic `TaskCreate` schema and creates the task in the database **for the logged-in user**.

**Expected scenario:** when sending *"Cadastre uma tarefa urgente chamada 'Revisar relatório financeiro' para o departamento Comercial"* ("Register an urgent task called 'Review financial report' for the Commercial department"), a task with `priority=urgent` and `department=Comercial` must be created for the authenticated user.

4. **Error handling:** if the LLM provider fails, the API must return a controlled error (e.g. `503`), not a generic 500.

> 💡 **You don't need to pay for an LLM API.** Pick one option in `.env`:
> - `LLM_MODEL=test`: PydanticAI's fake model, no key needed. It calls your tools with dummy data, which is great for development.
> - `LLM_MODEL=ollama:llama3.2`: a free local LLM via [Ollama](https://ollama.com).
> - `LLM_MODEL=google:gemini-3.8-flash`: Gemini, which has a free tier.
> - `LLM_MODEL=openai:<model>`: OpenAI.
>
> In **automated tests**, use PydanticAI's `TestModel` (see [tests/conftest.py](tests/conftest.py)). Tests must not call a real LLM.

### Part 3: AI Task Assistant (required)

Besides creating tasks, the AI must **help the user execute them**. In this part we mainly evaluate how you work with **context**: what information the LLM receives, where it comes from and what is left out.

1. **`POST /v1/tasks/{task_id}/assist` endpoint** (authenticated): the AI evaluates the task and returns a plan.
2. **A second PydanticAI agent** ([app/agent/task_assistant.py](app/agent/task_assistant.py)), separate from the chat agent, with **structured output** (`output_type`) using the `TaskAssistance` schema ([app/schemas/assistance.py](app/schemas/assistance.py)):
   - task summary and complexity (`low` / `medium` / `high`);
   - effort estimate in hours;
   - suggested priority, with a reason (does the current priority make sense?);
   - concrete, ordered steps to execute the task;
   - risks and attention points;
   - clarifying questions when information is missing.
3. **Context building** ([app/services/task_assistant_service.py](app/services/task_assistant_service.py)):
   - the task is loaded from the database **filtered by the logged-in user** (another user's task returns `404`);
   - include **small, relevant** extra context, e.g. up to 5 other open tasks of the same user in the same department;
   - inject this context through **dynamic instructions** (`@agent.instructions` + `RunContext`), separate from the static prompt;
   - do not send unnecessary or sensitive data to the LLM (password hashes, emails, other users' data, the whole table).
4. If the task has little information (e.g. no description), the AI must **say so and ask questions** instead of inventing details.
5. **Explain in the README** what information you sent to the LLM and why.

### Part 4: React Frontend (required)

The skeleton is in [frontend/](frontend/). Complete the parts marked with `TODO`:

1. A **login page** that stores the token and shows errors.
2. The user's **task list**, with loading, empty and error states.
3. A **form** to create tasks.
4. **Actions** to change the status and delete tasks.
5. A **chat panel** with the AI agent. When the agent creates a task, the list must be refreshed.
6. An **"Ask AI for help"** button on each task, opening the [TaskAssistantPanel](frontend/src/components/TaskAssistantPanel.tsx) with the evaluation and the execution plan.

On the backend, configure **CORSMiddleware** so the frontend can call the API (see the `TODO` in [app/main.py](app/main.py)).

We do not evaluate visual design. We evaluate **API consumption, state management and component organization**. Any library is welcome (Tailwind, MUI, React Query, etc.). If you prefer **Next.js**, you may replace the `frontend/` folder, as long as the project still runs with Docker Compose.

### Part 5: Quality and standards (required)

- **Automated tests** (pytest): at least login, CRUD, isolation between users, chat and the task assistant (with `TestModel`). The files in [tests/](tests/) list the suggested scenarios.
- **Structured logs** (JSON or key=value) in [app/core/logging.py](app/core/logging.py). Log at least task creation and agent calls.
- **API documentation**: docstrings on routes and `summary`/`description` where it makes sense. Remember that Swagger is generated from them.
- A **seed** with at least 2 users and some tasks ([seed/seed_data.py](seed/seed_data.py)). Document the credentials in the README.
- **Commits** that are small and clear, following [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `feat: add task CRUD endpoints`), on git-flow-style branches (`feature/...`).
- Code passing `ruff check .`.

### Nice to have (optional)

Only work on these after finishing the required scope. They are **not needed** to pass.

- An extra agent tool, e.g. `list_tasks` (*"what are my urgent tasks?"*).
- Cache the assistant's evaluation so the LLM is not called again until the task changes.
- Follow-up questions about the same task, keeping the conversation history (`message_history`).
- Filters and pagination on the task list.
- FastAPI **BackgroundTasks** to write an audit log when a task is created.
- **Redis** as a cache for the task list, invalidated on create, update or delete.
- Frontend tests (Vitest + Testing Library).
- React Query or a state management library.
- A CI pipeline (GitHub Actions) running lint and tests.

## Evaluation Criteria

| Criterion | Weight | What we look at |
|---|---|---|
| Backend: API and data | 30% | Async routes, use of `Depends`, Pydantic schemas, models, migration, layering (route → service → repository) |
| AI agents and context | 25% | Agent organization, prompt clarity, Pydantic-validated tool, structured output, context selection and building, LLM error handling |
| Security | 15% | JWT, hashed passwords, isolation between users |
| Frontend | 15% | API consumption, loading/error states, component organization |
| Quality | 15% | Tests, readability, logs, README, commit history |

## Technical Questionnaire

Answer in your own words, short and to the point. There is no single right answer: we want to understand your reasoning.

### 1. Async in FastAPI

What is the difference between declaring a route with `async def` and with `def` in FastAPI? In which situation can `async def` **hurt** performance?

**Answer:** _TODO_

### 2. Agent flow

Describe, step by step, what happens from the moment the user sends the chat message until the task is saved in the database. Where does Pydantic validation come in?

**Answer:** _TODO_

### 3. Assistant context

What information did you send to the LLM in the task assistant, and what did you decide to leave out? How does that choice affect answer quality, cost (tokens) and user privacy?

**Answer:** _TODO_

### 4. Security with AI

Why must the `user_id` used by the tool come from the request context (`ctx.deps`) and not from a parameter filled in by the LLM? What could go wrong in the second case?

**Answer:** _TODO_

### 5. Next steps

If you had one more week, what would you improve or add to the project, and why?

**Answer:** _TODO_

## How to Run

### Prerequisites

- Docker and Docker Compose
- (Optional) Python 3.11+ and Node.js 20+ to run outside Docker

### With Docker Compose (recommended)

```bash
cp .env.example .env
docker compose up --build
```

| Service | URL |
|---|---|
| API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| Frontend | http://localhost:5173 |
| PostgreSQL | `localhost:5433` (change it with `POSTGRES_HOST_PORT` if the port is in use) |

Useful commands while the containers are running:

```bash
docker compose exec api alembic revision --autogenerate -m "create users and tasks tables"
docker compose exec api alembic upgrade head
docker compose exec api python -m seed.seed_data
docker compose exec api pytest -v
docker compose exec api ruff check .
```

### Locally (API outside Docker)

```bash
# Start only the database
docker compose up db -d

# In .env, point to the exposed port:
# DATABASE_URL=postgresql+asyncpg://app:app@localhost:5433/desafio

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt

alembic upgrade head
python -m seed.seed_data
uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

## Project Structure

```
app/
├── main.py                  # FastAPI entrypoint (TODO: CORS and logging)
├── config.py                # ✅ Settings (pydantic-settings)
├── api/
│   ├── deps.py              # ✅ get_db · TODO: get_current_user
│   └── v1/
│       ├── router.py        # ✅ Route aggregator
│       └── endpoints/       # TODO: auth, tasks, chat
├── core/
│   ├── database.py          # ✅ AsyncEngine and session factory
│   ├── security.py          # ✅ JWT and password hashing
│   └── logging.py           # TODO: structured logs
├── models/                  # ✅ User · TODO: Task
├── schemas/                 # TODO: Pydantic schemas
├── repositories/            # TODO: data access
├── services/                # TODO: business rules
└── agent/                   # TODO: chat agent, task assistant, tools and prompts
frontend/
└── src/
    ├── api/                 # ✅ client.ts · TODO: auth, tasks, chat
    ├── pages/               # Login and Tasks
    ├── components/          # TaskForm, TaskList, ChatPanel, TaskAssistantPanel
    └── types.ts             # Types mirroring the API schemas
tests/                       # ✅ conftest + example · TODO: remaining tests
seed/                        # TODO: initial data
```

## Submission

1. Create a **public** GitHub repository from this project.
2. Update this README with:
   - the **seed credentials**;
   - your **questionnaire answers**;
   - the decisions you made and anything left out (if applicable).
3. Send us the repository link.

### Checklist

- [ ] JWT authentication (register, login, me)
- [ ] Task CRUD with per-user isolation
- [ ] Alembic migration
- [ ] PydanticAI agent with the `create_task` tool
- [ ] Task assistant with structured output and context explained in the README
- [ ] Frontend: login, list, create, actions, chat and AI help
- [ ] Automated tests (including chat and assistant with `TestModel`)
- [ ] Structured logs
- [ ] Seed with documented credentials
- [ ] Questionnaire answered

Good luck! 🚀
