# Party RSVP

Simple RSVP web application for kids birthday parties.

## Description

Party RSVP is a lightweight FastAPI project for collecting and viewing birthday party responses.
It serves an invite page for guests, accepts RSVP submissions, stores them in SQLite, and provides an admin dashboard with response counts.

## Features

- Invite page at `/invite/{invite_id}`
- RSVP submission API at `POST /api/rsvp`
- Admin dashboard at `/admin`
- Admin responses API at `GET /api/responses/{invite_id}`
- SQLite persistence (`backend/rsvp.db`)
- FastAPI backend with modular architecture

## Project Structure

```text
backend/
  app/
    api/
      admin.py
      invite.py
      rsvp.py
    db/
      database.py
    models/
      rsvp.py
    schemas/
      rsvp.py
    services/
      rsvp_service.py
    main.py
  requirements.txt
  rsvp.db

frontend/
  pages/
    invite.html
    admin.html

database/
  schema.sql
```

## How to Run Locally

1. Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

2. Start the server:

```bash
cd backend
uvicorn app.main:app --reload
```

3. Open the app:

- Invite page: `http://127.0.0.1:8000/invite/test123`
- Admin dashboard: `http://127.0.0.1:8000/admin`

## API Endpoints

- `GET /api/invite/{invite_id}`
  - Returns invitation JSON payload for the invite page.
- `POST /api/rsvp`
  - Accepts JSON:

```json
{
  "inviteId": "test123",
  "response": "yes"
}
```

  - Returns:

```json
{
  "status": "received"
}
```

- `GET /api/responses/{invite_id}`
  - Returns all stored responses for a given invite ID.

## Example Invite Link

`http://127.0.0.1:8000/invite/test123`

## License

MIT
