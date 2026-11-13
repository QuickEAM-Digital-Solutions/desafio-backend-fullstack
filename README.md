# Desafio Técnico — Desenvolvedor(a) FullStack Júnior (Foco em Backend · Python / AI)

> 🇺🇸 English version: [README.en-us.md](README.en-us.md)

## Objetivo

Você vai construir um **gerenciador de tarefas com assistente de IA**: cada usuário faz login, gerencia as próprias tarefas por uma interface React, pode pedir a um agente de IA, em linguagem natural, que cadastre tarefas por ele, e pode pedir à IA que **avalie uma tarefa e monte um plano para executá-la**.

O foco do desafio é o **backend**. Queremos avaliar sua capacidade de construir uma API limpa, validada e bem organizada, além de integrar um agente de IA a um fluxo real do produto. O frontend é mais simples e serve para mostrar que você sabe consumir a sua própria API.

Não esperamos um sistema perfeito. Preferimos **código simples, legível e bem explicado** a muitas funcionalidades pela metade. Se não conseguir terminar algo, conte no README o que faltou e como você faria.

## Stack Tecnológica

| Camada | Tecnologias |
|---|---|
| Linguagem | Python 3.11+ (`async`/`await` e type hints) |
| Framework Web | FastAPI (rotas assíncronas, `Depends`, Swagger automático) |
| Validação | Pydantic v2 |
| IA | PydanticAI (agente + tool calling) |
| Banco de Dados | PostgreSQL + SQLAlchemy 2.0 (assíncrono) + Alembic |
| Frontend | React + TypeScript (Vite). **Next.js também é aceito** |
| Infra | Docker e Docker Compose |
| Padrões | PEP8 (ruff), código e logs em inglês, commits padronizados |

## O que já vem pronto

Para você focar no que importa, o repositório já traz:

- ✅ **Docker Compose** com API, PostgreSQL e frontend (`docker compose up --build`)
- ✅ **Configurações** tipadas com `pydantic-settings` ([app/config.py](app/config.py))
- ✅ **Conexão assíncrona com o banco** ([app/core/database.py](app/core/database.py)) e dependência `get_db()` ([app/api/deps.py](app/api/deps.py))
- ✅ **Utilitários de segurança**: hash de senha (bcrypt) e criação/validação de JWT ([app/core/security.py](app/core/security.py))
- ✅ **Model `User`** pronto, para servir de referência ([app/models/user.py](app/models/user.py))
- ✅ **Alembic** configurado e um **router** v1 já registrado
- ✅ **Cliente HTTP de testes** (`async_client`) e um teste de exemplo ([tests/](tests/))
- ✅ **Esqueleto do frontend** em React + TypeScript que já compila, com cliente HTTP, telas e componentes ([frontend/](frontend/))

Cada arquivo que você precisa completar tem um comentário no topo com **"You should implement here"** explicando o que é esperado.

## Escopo do Desafio

### Parte 1: Autenticação e CRUD de Tarefas (obrigatório)

1. **Autenticação JWT**
   - `POST /v1/auth/register`: cria um usuário (senha armazenada com hash).
   - `POST /v1/auth/login`: valida as credenciais e retorna um token JWT.
   - `GET /v1/auth/me`: retorna o usuário autenticado.
   - Implemente a dependência `get_current_user()` em [app/api/deps.py](app/api/deps.py).

2. **CRUD de Tarefas** (`/v1/tasks`)
   - Criar, listar, buscar por ID, atualizar parcialmente (`PATCH`) e excluir.
   - Campos: `title`, `description`, `status` (`pending` / `in_progress` / `completed`), `priority` (`low` / `medium` / `high` / `urgent`), `department`, `created_at` e `updated_at`.
   - Validação com **schemas Pydantic v2** e `response_model` nas rotas.

3. **Isolamento por usuário** 🔒
   - Cada tarefa pertence a um usuário (`user_id`).
   - Um usuário **nunca** pode ver, alterar ou excluir tarefas de outro usuário. Acessar a tarefa de outro usuário deve retornar `404`.

4. **Banco de dados**
   - Model `Task` com SQLAlchemy 2.0 (estilo `Mapped[...]`).
   - Pelo menos **uma migration Alembic** criando as tabelas.

### Parte 2: Agente de IA com PydanticAI (obrigatório)

1. **Endpoint `POST /v1/chat`** (autenticado): recebe a mensagem do usuário e retorna a resposta do agente.
2. **Agente PydanticAI** com um system prompt claro ([app/agent/](app/agent/)).
3. **Tool `create_task`**: o agente extrai as informações da mensagem, valida com o schema Pydantic `TaskCreate` e cria a tarefa no banco **para o usuário logado**.

**Cenário esperado:** ao enviar *"Cadastre uma tarefa urgente chamada 'Revisar relatório financeiro' para o departamento Comercial"*, deve surgir uma tarefa com `priority=urgent` e `department=Comercial` para o usuário autenticado.

4. **Tratamento de erros:** se o provedor da LLM falhar, a API deve responder com um erro controlado (ex.: `503`), e não com um erro 500 genérico.

> 💡 **Você não precisa pagar por uma API de LLM.** Escolha uma opção no `.env`:
> - `LLM_MODEL=test`: modelo falso do PydanticAI, sem chave. Ele chama suas tools com dados fictícios, o que é ótimo para desenvolver.
> - `LLM_MODEL=ollama:llama3.2`: LLM local e gratuito via [Ollama](https://ollama.com).
> - `LLM_MODEL=google:gemini-3.8-flash`: Gemini, que tem plano gratuito.
> - `LLM_MODEL=openai:<modelo>`: OpenAI.
>
> Nos **testes automatizados**, use o `TestModel` do PydanticAI (veja [tests/conftest.py](tests/conftest.py)). Os testes não devem chamar uma LLM real.

### Parte 3: Assistente de Tarefas com IA (obrigatório)

Além de criar tarefas, a IA deve **ajudar o usuário a executá-las**. Nesta parte avaliamos principalmente como você trabalha com **contexto**: que informações a LLM recebe, de onde elas vêm e o que fica de fora.

1. **Endpoint `POST /v1/tasks/{task_id}/assist`** (autenticado): a IA avalia a tarefa e retorna um plano.
2. **Um segundo agente PydanticAI** ([app/agent/task_assistant.py](app/agent/task_assistant.py)), separado do agente do chat, com **saída estruturada** (`output_type`) usando o schema `TaskAssistance` ([app/schemas/assistance.py](app/schemas/assistance.py)):
   - resumo da tarefa e complexidade (`low` / `medium` / `high`);
   - estimativa de esforço em horas;
   - prioridade sugerida, com justificativa (a prioridade atual faz sentido?);
   - passos concretos e ordenados para executar a tarefa;
   - riscos e pontos de atenção;
   - perguntas de esclarecimento, quando faltar informação.
3. **Montagem do contexto** ([app/services/task_assistant_service.py](app/services/task_assistant_service.py)):
   - a tarefa é buscada no banco **filtrando pelo usuário logado** (tarefa de outro usuário retorna `404`);
   - inclua um contexto complementar **pequeno e relevante**, por exemplo até 5 outras tarefas abertas do mesmo usuário e do mesmo departamento;
   - injete esse contexto via **instruções dinâmicas** (`@agent.instructions` + `RunContext`), separado do prompt fixo;
   - não envie dados desnecessários ou sensíveis à LLM (hash de senha, e-mail, dados de outros usuários, a tabela inteira).
4. Se a tarefa tiver pouca informação (ex.: sem descrição), a IA deve **dizer isso e fazer perguntas**, em vez de inventar detalhes.
5. **Explique no README** quais informações você enviou à LLM e por quê.

### Parte 4: Frontend React (obrigatório)

O esqueleto já está em [frontend/](frontend/). Complete os pontos marcados com `TODO`:

1. **Tela de login** que salva o token e mostra os erros.
2. **Lista de tarefas** do usuário, com estados de carregando, vazio e erro.
3. **Formulário** para criar tarefas.
4. **Ações** para alterar o status e excluir tarefas.
5. **Painel de chat** com o agente de IA. Quando o agente criar uma tarefa, a lista deve ser atualizada.
6. Botão **"Pedir ajuda à IA"** em cada tarefa, abrindo o painel [TaskAssistantPanel](frontend/src/components/TaskAssistantPanel.tsx) com a avaliação e o plano de execução.

No backend, configure o **CORSMiddleware** para que o frontend consiga chamar a API (veja o `TODO` em [app/main.py](app/main.py)).

Não avaliamos design. Avaliamos **consumo da API, gerenciamento de estado e organização dos componentes**. Pode usar qualquer biblioteca (Tailwind, MUI, React Query etc.). Se preferir **Next.js**, pode substituir a pasta `frontend/`, desde que o projeto continue rodando pelo Docker Compose.

### Parte 5: Qualidade e padrões (obrigatório)

- **Testes automatizados** (pytest): pelo menos login, CRUD, isolamento entre usuários, chat e assistente de tarefas (com `TestModel`). Os arquivos em [tests/](tests/) listam os cenários sugeridos.
- **Logs estruturados** (JSON ou chave=valor) em [app/core/logging.py](app/core/logging.py). Registre pelo menos a criação de tarefas e as chamadas ao agente.
- **Documentação da API**: docstrings nas rotas e `summary`/`description` quando fizer sentido. Lembre que o Swagger é gerado a partir delas.
- **Seed** com pelo menos 2 usuários e algumas tarefas ([seed/seed_data.py](seed/seed_data.py)). Informe as credenciais no README.
- **Commits** pequenos e com mensagens claras, seguindo o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/) (ex.: `feat: add task CRUD endpoints`), em branches no estilo git flow (`feature/...`).
- Código passando no `ruff check .`.

### Diferenciais (opcionais)

Só faça estes itens depois de concluir o obrigatório. Eles **não são necessários** para ser aprovado.

- Tool extra no agente, por exemplo `list_tasks` (*"quais são minhas tarefas urgentes?"*).
- Cache da avaliação do assistente, para não chamar a LLM de novo enquanto a tarefa não mudar.
- Perguntas de acompanhamento sobre a mesma tarefa, mantendo o histórico da conversa (`message_history`).
- Filtros e paginação na listagem de tarefas.
- **BackgroundTasks** do FastAPI para registrar um log de auditoria quando uma tarefa for criada.
- **Redis** como cache da listagem de tarefas, com invalidação ao criar, editar ou excluir.
- Testes no frontend (Vitest + Testing Library).
- Uso de React Query ou de um gerenciador de estado.
- Pipeline de CI (GitHub Actions) rodando lint e testes.

## Critérios de Avaliação

| Critério | Peso | O que observamos |
|---|---|---|
| Backend: API e dados | 30% | Rotas assíncronas, uso de `Depends`, schemas Pydantic, models, migration, separação em camadas (rota → service → repository) |
| Agentes de IA e contexto | 25% | Organização dos agentes, clareza dos prompts, tool validada com Pydantic, saída estruturada, escolha e montagem do contexto, tratamento de erros da LLM |
| Segurança | 15% | JWT, senhas com hash, isolamento entre usuários |
| Frontend | 15% | Consumo da API, estados de carregando/erro, organização dos componentes |
| Qualidade | 15% | Testes, legibilidade, logs, README, histórico de commits |

## Questionário Técnico

Responda com suas palavras, de forma curta e direta. Não existe resposta única certa: queremos entender o seu raciocínio.

### 1. Async no FastAPI

Qual a diferença entre declarar uma rota com `async def` e com `def` no FastAPI? Em que situação usar `async def` pode **piorar** a performance?

**Resposta:** _TODO_

### 2. Fluxo do agente

Descreva, passo a passo, o que acontece desde o momento em que o usuário envia a mensagem no chat até a tarefa ser salva no banco. Onde entra a validação do Pydantic nesse fluxo?

**Resposta:** _TODO_

### 3. Contexto do assistente

Quais informações você enviou à LLM no assistente de tarefas e o que decidiu deixar de fora? Como essa escolha afeta a qualidade da resposta, o custo (tokens) e a privacidade do usuário?

**Resposta:** _TODO_

### 4. Segurança com IA

Por que o `user_id` usado pela tool deve vir do contexto da requisição (`ctx.deps`) e não de um parâmetro preenchido pela LLM? O que poderia dar errado no segundo caso?

**Resposta:** _TODO_

### 5. Próximos passos

Se você tivesse mais uma semana, o que melhoraria ou adicionaria no projeto? Por quê?

**Resposta:** _TODO_

## Como Executar

### Pré-requisitos

- Docker e Docker Compose
- (Opcional) Python 3.11+ e Node.js 20+ para rodar fora do Docker

### Com Docker Compose (recomendado)

```bash
cp .env.example .env
docker compose up --build
```

| Serviço | URL |
|---|---|
| API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| Frontend | http://localhost:5173 |
| PostgreSQL | `localhost:5433` (mude com `POSTGRES_HOST_PORT` se a porta estiver ocupada) |

Comandos úteis com os containers rodando:

```bash
docker compose exec api alembic revision --autogenerate -m "create users and tasks tables"
docker compose exec api alembic upgrade head
docker compose exec api python -m seed.seed_data
docker compose exec api pytest -v
docker compose exec api ruff check .
```

### Localmente (sem Docker para a API)

```bash
# Suba apenas o banco
docker compose up db -d

# No .env, aponte para a porta exposta:
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

## Estrutura do Projeto

```
app/
├── main.py                  # Entrypoint FastAPI (TODO: CORS e logging)
├── config.py                # ✅ Configurações (pydantic-settings)
├── api/
│   ├── deps.py              # ✅ get_db · TODO: get_current_user
│   └── v1/
│       ├── router.py        # ✅ Agregador de rotas
│       └── endpoints/       # TODO: auth, tasks, chat
├── core/
│   ├── database.py          # ✅ AsyncEngine e session factory
│   ├── security.py          # ✅ JWT e hash de senha
│   └── logging.py           # TODO: logs estruturados
├── models/                  # ✅ User · TODO: Task
├── schemas/                 # TODO: schemas Pydantic
├── repositories/            # TODO: acesso a dados
├── services/                # TODO: regras de negócio
└── agent/                   # TODO: agente do chat, assistente de tarefas, tools e prompts
frontend/
└── src/
    ├── api/                 # ✅ client.ts · TODO: auth, tasks, chat
    ├── pages/               # Login e Tarefas
    ├── components/          # TaskForm, TaskList, ChatPanel, TaskAssistantPanel
    └── types.ts             # Tipos espelhando os schemas da API
tests/                       # ✅ conftest + exemplo · TODO: demais testes
seed/                        # TODO: dados iniciais
```

## Entrega

1. Crie um repositório **público** no GitHub a partir deste projeto.
2. Atualize este README com:
   - as **credenciais do seed**;
   - as **respostas do questionário**;
   - as decisões que você tomou e o que ficou de fora (se for o caso).
3. Envie o link do repositório.

### Checklist

- [ ] Autenticação JWT (register, login, me)
- [ ] CRUD de tarefas com isolamento por usuário
- [ ] Migration Alembic
- [ ] Agente PydanticAI com a tool `create_task`
- [ ] Assistente de tarefas com saída estruturada e contexto explicado no README
- [ ] Frontend: login, lista, criação, ações, chat e ajuda da IA
- [ ] Testes automatizados (incluindo chat e assistente com `TestModel`)
- [ ] Logs estruturados
- [ ] Seed com credenciais documentadas
- [ ] Questionário respondido

Boa sorte! 🚀
