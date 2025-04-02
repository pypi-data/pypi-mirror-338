init:
	uv sync --dev

test:
	uv run pytest -v -p pytest_cov

lint:
	uv run ruff format
	uv run ruff check --fix
