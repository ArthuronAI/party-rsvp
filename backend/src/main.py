from pathlib import Path
from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .database import get_connection, init_db

app = FastAPI()

MOCK_INVITATION = {
    "childName": "Emma",
    "date": "May 20",
    "time": "3:00 PM",
    "location": "123 Main St",
}

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INVITE_PAGE_PATH = PROJECT_ROOT / "frontend" / "pages" / "invite.html"
ADMIN_PAGE_PATH = PROJECT_ROOT / "frontend" / "pages" / "admin.html"


class RSVPRequest(BaseModel):
    inviteId: str
    response: Literal["yes", "no"]


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/")
def read_root():
    return MOCK_INVITATION


@app.get("/api/invite/{invite_id}")
def get_invite(invite_id: str):
    return {"inviteId": invite_id, **MOCK_INVITATION}


@app.get("/invite/{invite_id}", response_class=HTMLResponse)
def read_invite_page(invite_id: str):
    if not INVITE_PAGE_PATH.exists():
        raise HTTPException(status_code=404, detail="Invite page not found")

    return INVITE_PAGE_PATH.read_text(encoding="utf-8")


@app.get("/admin", response_class=HTMLResponse)
def read_admin_page():
    if not ADMIN_PAGE_PATH.exists():
        raise HTTPException(status_code=404, detail="Admin page not found")

    return ADMIN_PAGE_PATH.read_text(encoding="utf-8")


@app.post("/api/rsvp")
def submit_rsvp(payload: RSVPRequest):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO rsvp (invite_id, response) VALUES (?, ?)",
            (payload.inviteId, payload.response),
        )
        conn.commit()

    return {"status": "received"}


@app.get("/api/responses/{invite_id}")
def get_responses(invite_id: str):
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT response, created_at
            FROM rsvp
            WHERE invite_id = ?
            ORDER BY created_at ASC, id ASC
            """,
            (invite_id,),
        ).fetchall()

    responses = [
        {
            "response": row["response"],
            "created_at": row["created_at"],
        }
        for row in rows
    ]

    return {"inviteId": invite_id, "responses": responses}
