# FinChoice MVP

FinChoice — независимая витрина для сравнения демонстрационных предложений финансовых организаций. Сервис не выдаёт займы, не собирает персональные данные и не принимает решения по заявкам.

## Структура и стек

- `backend/`: FastAPI, SQLAlchemy 2.x async, PostgreSQL, Alembic, Pydantic Settings, uv.
- `frontend/`: React, TypeScript, Vite и Axios.
- `docker-compose.yml`: PostgreSQL 17, API и frontend.

Архитектура API: router → service → repository → SQLAlchemy → PostgreSQL.

## Локальный запуск

Установите [uv](https://docs.astral.sh/uv/getting-started/installation/) и Node.js 22+.

```powershell
docker compose up -d postgres
Copy-Item backend/.env.example backend/.env
cd backend
uv sync
uv run alembic upgrade head
uv run python -m app.db.seed
uv run uvicorn app.main:app --reload
```

Во втором терминале:

```powershell
cd frontend
npm install
npm run dev
```

Откройте `http://localhost:5173`. Документация API: `http://localhost:8000/docs` и `/redoc`. Полный Docker-запуск: `docker compose up --build`; после первого запуска примените миграцию и seed в контейнере backend.

## API

- `GET /api/v1/health` — проверка сервиса.
- `GET /api/v1/offers?max_amount=50000&max_term_days=30&sort=popularity` — список и фильтрация. Доступные сортировки: `popularity`, `max_amount`, `max_term`.
- `POST /api/v1/offers/{offer_id}/click` — фиксирует только ID предложения и время перехода; IP и персональные данные не сохраняются.

## Данные и production

Шесть вымышленных предложений находятся в `backend/app/db/seed.py`. Новое предложение добавляется в этот список для demo-режима или непосредственно в таблицу `loan_offers`. В дальнейшем реальные CPA-offers нужно подключать на уровне repository/service, оставляя frontend зависимым только от API.

Перед production: подтвердите юридические тексты и рекламные маркировки, настройте реальные внешние URL и CORS, добавьте мониторинг, защищённые секреты, резервное копирование PostgreSQL и политику обработки данных.
