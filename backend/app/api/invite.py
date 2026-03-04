from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

router = APIRouter()

MOCK_INVITATION = {
    "childName": "Emma",
    "date": "May 20",
    "time": "3:00 PM",
    "location": "123 Main St",
}

PROJECT_ROOT = Path(__file__).resolve().parents[3]
INVITE_PAGE_PATH = PROJECT_ROOT / "frontend" / "pages" / "invite.html"


@router.get("/")
def read_root():
    return MOCK_INVITATION


@router.get("/api/invite/{invite_id}")
def get_invite(invite_id: str):
    return {"inviteId": invite_id, **MOCK_INVITATION}


@router.get("/invite/{invite_id}", response_class=HTMLResponse)
def read_invite_page(invite_id: str):
    if not INVITE_PAGE_PATH.exists():
        raise HTTPException(status_code=404, detail="Invite page not found")

    return INVITE_PAGE_PATH.read_text(encoding="utf-8")
