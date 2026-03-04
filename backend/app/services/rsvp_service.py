from ..db.database import get_connection


def create_rsvp(invite_id: str, response: str) -> None:
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO rsvp (invite_id, response) VALUES (?, ?)",
            (invite_id, response),
        )
        conn.commit()


def get_responses_by_invite(invite_id: str) -> list[dict[str, str]]:
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

    return [
        {
            "response": row["response"],
            "created_at": row["created_at"],
        }
        for row in rows
    ]
