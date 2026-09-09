# AI Expense Tracker — Project State

## Goal
Build an AI-powered expense tracker API using FastAPI, SQLAlchemy, and SQLite (later PostgreSQL), with testing, authentication, and deployment.

---

## Milestones

### 1. Core API (FastAPI + Basic CRUD)
- [x] FastAPI setup
- [x] User model (in-memory → DB migration started)
- [x] Expense model (SQLAlchemy)
- [x] SQLite integration
- [x] Basic routers structure
- [ ] Complete Expense CRUD (Create, Read, Update, Delete)
- [ ] Clean API responses (remove raw ORM leakage)

---

### 2. Database Design (SQLAlchemy)
- [ ] User ↔ Expense relationship (one-to-many)
- [ ] Foreign keys properly enforced
- [ ] Cascade rules (delete user → delete expenses or restrict)asdsda
- [ ] Migrations (Alembic setup)

---

### 3. Testing Layer (pytest)
- [x] Basic health check tests
- [ ] User CRUD tests
- [ ] Expense CRUD tests
- [ ] Database dependency override tests
- [ ] Test isolation (clean DB per test run)
- [ ] Coverage baseline established

---

### 4. Authentication (Not started)
- [ ] JWT authentication
- [ ] Login / register endpoints
- [ ] Protected routes
- [ ] Current user dependency (`get_current_user`)

---

### 5. Production Readiness
- [ ] Docker setup
- [ ] Environment configuration (`.env`)
- [ ] CI pipeline (GitHub Actions)
- [ ] Logging setup
- [ ] Error handling standardization

---

## Current Focus
Fix testing dependencies (httpx/TestClient issue) and complete Expense CRUD endpoints.

---

## Blocked / Questions
- SQLAlchemy relationship design for User ↔ Expense
- Proper test database setup strategy
- Whether to introduce authentication before expanding features

---

## Done Log
- FastAPI project initialized
- User CRUD partially implemented
- Expense model created
- SQLite connected via SQLAlchemy
- Basic routing structure introduced
- Health and readiness endpoints implemented
- Initial pytest setup completed

---

## Rules Going Forward
- Do not start new features without updating this file
- Keep "Current Focus" limited to one or two tasks
- Move completed tasks immediately to "Done Log"
- If unsure, write it under "Blocked / Questions" instead of implementing
