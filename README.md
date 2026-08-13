# SkillBytes Admin Panel

Internal admin panel for staff accounts (managers, teachers, and admins).
Built with **React + TypeScript** on the frontend and **FastAPI + MongoDB**
on the backend.

## Stack

- `frontend/` — React 18, TypeScript, Vite
- `backend/` — FastAPI, Motor (async MongoDB driver), Pydantic

## Getting started

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in MONGODB_URI
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env   # set VITE_API_BASE_URL if not localhost:8000
npm run dev
```

Frontend runs on `http://localhost:5173`, backend on `http://localhost:8000`.

## API

`GET /api/users?page=1&limit=20` — paginated list of staff users (manager,
teacher, admin roles only; plain `user` accounts are excluded since this is
an internal panel).

## Known issue

Users have reported that the **Users** page in the admin panel intermittently
fails to load, returning a **504 Gateway Timeout**. It seems to happen more
often as the user base has grown. Investigate and fix.
# Skillbytes-Interview-Find-Error
