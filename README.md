# 🎫 Helpdesk API (Flask + PostgreSQL + Docker)

🌐 [Español](#español) | [English](#english) | [Português](#português)

---

## 🇪🇸 Español

Mini API REST de helpdesk (tickets de soporte) con **Flask + PostgreSQL + Docker**, con pruebas automatizadas en **pytest** ejecutadas en CI con **GitHub Actions** en cada push y pull request.

### Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/tickets` | Lista tickets (filtro opcional `?status=`) |
| POST | `/tickets` | Crea un ticket (`title` obligatorio) |
| GET | `/tickets/<id>` | Detalle de un ticket |
| PATCH | `/tickets/<id>` | Actualiza estado, prioridad, título o descripción |
| DELETE | `/tickets/<id>` | Elimina un ticket |

Estados: `open`, `in_progress`, `closed` · Prioridades: `low`, `medium`, `high`

### Ejecutar con Docker

```bash
docker compose up --build
```

La API queda en `http://localhost:5000` con PostgreSQL incluido (no hace falta instalar nada más).

### Ejecutar las pruebas

```bash
pip install -r requirements-dev.txt
pytest -v
```

Resultado: **10 pruebas, todas en verde** ✅ (las pruebas usan SQLite en memoria; producción usa PostgreSQL vía `DATABASE_URL`)

### Estructura

```
├── app/
│   ├── __init__.py      # App factory
│   ├── models.py        # Modelo Ticket (SQLAlchemy)
│   └── routes.py        # Endpoints del CRUD
├── tests/               # 10 pruebas del CRUD y validaciones
├── Dockerfile
├── docker-compose.yml   # API + PostgreSQL
└── .github/workflows/   # CI: pytest en cada push/PR
```

---

## 🇬🇧 English

Mini REST helpdesk API (support tickets) with **Flask + PostgreSQL + Docker**, with automated **pytest** tests running in CI with **GitHub Actions** on every push and pull request.

### Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/tickets` | List tickets (optional `?status=` filter) |
| POST | `/tickets` | Create a ticket (`title` required) |
| GET | `/tickets/<id>` | Ticket detail |
| PATCH | `/tickets/<id>` | Update status, priority, title or description |
| DELETE | `/tickets/<id>` | Delete a ticket |

Statuses: `open`, `in_progress`, `closed` · Priorities: `low`, `medium`, `high`

### Run with Docker

```bash
docker compose up --build
```

The API runs at `http://localhost:5000` with PostgreSQL included (nothing else to install).

### Run the tests

```bash
pip install -r requirements-dev.txt
pytest -v
```

Result: **10 tests, all passing** ✅ (tests use in-memory SQLite; production uses PostgreSQL via `DATABASE_URL`)

### Project layout

```
├── app/
│   ├── __init__.py      # App factory
│   ├── models.py        # Ticket model (SQLAlchemy)
│   └── routes.py        # CRUD endpoints
├── tests/               # 10 tests covering CRUD and validation
├── Dockerfile
├── docker-compose.yml   # API + PostgreSQL
└── .github/workflows/   # CI: pytest on every push/PR
```

---

## 🇧🇷 Português

Mini API REST de helpdesk (tickets de suporte) com **Flask + PostgreSQL + Docker**, com testes automatizados em **pytest** rodando em CI com **GitHub Actions** a cada push e pull request.

### Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/tickets` | Lista tickets (filtro opcional `?status=`) |
| POST | `/tickets` | Cria um ticket (`title` obrigatório) |
| GET | `/tickets/<id>` | Detalhe de um ticket |
| PATCH | `/tickets/<id>` | Atualiza status, prioridade, título ou descrição |
| DELETE | `/tickets/<id>` | Remove um ticket |

Status: `open`, `in_progress`, `closed` · Prioridades: `low`, `medium`, `high`

### Rodar com Docker

```bash
docker compose up --build
```

A API sobe em `http://localhost:5000` com PostgreSQL incluído (não precisa instalar mais nada).

### Rodar os testes

```bash
pip install -r requirements-dev.txt
pytest -v
```

Resultado: **10 testes, todos passando** ✅ (os testes usam SQLite em memória; produção usa PostgreSQL via `DATABASE_URL`)

### Estrutura

```
├── app/
│   ├── __init__.py      # App factory
│   ├── models.py        # Modelo Ticket (SQLAlchemy)
│   └── routes.py        # Endpoints do CRUD
├── tests/               # 10 testes do CRUD e validações
├── Dockerfile
├── docker-compose.yml   # API + PostgreSQL
└── .github/workflows/   # CI: pytest a cada push/PR
```
