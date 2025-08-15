upgrade:
	uv run alembic upgrade head

downgrade:
	uv run alembic downgrade base

db:
	make downgrade upgrade

seed:
	uv run seed.py

reseed:
	make db seed

format:
	uv run ruff format
