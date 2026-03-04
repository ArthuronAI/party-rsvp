from dataclasses import dataclass


@dataclass
class RSVP:
    id: int
    invite_id: str
    response: str
    created_at: str
