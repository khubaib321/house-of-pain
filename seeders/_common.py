import sqlalchemy as _sa
import pydantic as _pydantic

from modules import db as _db
from modules.base import model as _model


def insert_batch(
    model: _model.BaseModel, items: list[_pydantic.BaseModel], start: int
) -> None:
    if not items:
        return

    to_insert = [user.model_dump() for user in items]

    with _db.SessionMakerSync() as session:
        session.execute(_sa.insert(model).values(to_insert))
        session.commit()

    print(f"\t✔︎ Inserted chunk from {start} to {start + len(items)}")
