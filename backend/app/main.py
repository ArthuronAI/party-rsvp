from fastapi import FastAPI

from .api import admin, invite, rsvp
from .db.database import init_db

app = FastAPI()


@app.on_event("startup")
def startup_event() -> None:
    init_db()


app.include_router(invite.router)
app.include_router(rsvp.router)
app.include_router(admin.router)
