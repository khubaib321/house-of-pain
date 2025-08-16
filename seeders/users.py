import random as _rand
import sqlalchemy as _sa
import concurrent.futures as _futures

from modules import db as _db
from modules.users import enums as _enums
from modules.users import domain as _domain
from modules.users import models as _models

from . import _common


def _get_base_user(idx: int) -> _domain.BaseUserWithPassword:
    return _domain.BaseUserWithPassword(
        password="",
        email=f"user{idx}@email.com",
        first_name="Test",
        middle_name="User",
        last_name=f"No. {idx}",
        status=_rand.choice(list(_enums.UserStatus)),
    )


async def create_test_users(*, count: int) -> None:
    print(f"👀 {count:,} users to add")

    start_idx = 0
    async with _db.SessionMaker() as session:
        query = await session.execute(_sa.select(_sa.func.max(_models.User.id)))
        start_idx = query.scalar() or 0

    print(f"👀 {start_idx:,} existing users")

    users: list[_domain.BaseUser] = []
    for i in range(count):
        idx = i + start_idx
        users.append(_get_base_user(idx))

    batch_size = 65535 // 6
    print("👀 Batch size:", batch_size)

    with _futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = []
        for k in range(0, count, batch_size):
            start = k
            end = k + batch_size
            chunk = users[start:end]
            futures.append(
                executor.submit(
                    _common.insert_batch,
                    start=start,
                    items=chunk,
                    model=_models.User,
                )
            )

        _futures.wait(futures)

    print("✅ Done")
