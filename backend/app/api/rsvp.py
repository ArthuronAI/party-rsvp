from fastapi import APIRouter

from ..schemas.rsvp import RSVPRequest, RSVPResponse
from ..services.rsvp_service import create_rsvp

router = APIRouter()


@router.post("/api/rsvp", response_model=RSVPResponse)
def submit_rsvp(payload: RSVPRequest):
    create_rsvp(payload.inviteId, payload.response)
    return RSVPResponse(status="received")
