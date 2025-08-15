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

run:
	uvicorn main:app --loop uvloop --host 0.0.0.0 --port 8192

dev:
	uv sync --active
	uvicorn main:app --loop uvloop --host 0.0.0.0 --port 8192 --reload
