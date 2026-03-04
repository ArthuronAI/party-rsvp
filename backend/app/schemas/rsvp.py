from typing import Literal

from pydantic import BaseModel


class RSVPRequest(BaseModel):
    inviteId: str
    response: Literal["yes", "no"]


class RSVPResponse(BaseModel):
    status: str
