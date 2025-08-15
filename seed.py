import asyncio as _asyncio
from seeders import users as _users_seeder


async def seed_all() -> None:
    await _users_seeder.create_test_users(count=1_000_000)


if __name__ == "__main__":
    _asyncio.run(seed_all())
