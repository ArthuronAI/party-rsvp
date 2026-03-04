from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from ..services.rsvp_service import get_responses_by_invite

router = APIRouter()

PROJECT_ROOT = Path(__file__).resolve().parents[3]
ADMIN_PAGE_PATH = PROJECT_ROOT / "frontend" / "pages" / "admin.html"


@router.get("/admin", response_class=HTMLResponse)
def read_admin_page():
    if not ADMIN_PAGE_PATH.exists():
        raise HTTPException(status_code=404, detail="Admin page not found")

    return ADMIN_PAGE_PATH.read_text(encoding="utf-8")


@router.get("/api/responses/{invite_id}")
def get_responses(invite_id: str):
    responses = get_responses_by_invite(invite_id)
    return {"inviteId": invite_id, "responses": responses}
