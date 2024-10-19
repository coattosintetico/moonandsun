format:
	uv run ruff check --fix
	uv run ruff format
.PHONY: format

phases:
	uv run python -m src.phases.main
.PHONY: phases

riseandset:
	uv run python -m src.riseandset.main
.PHONY: riseandset
