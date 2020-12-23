#
# Copyright (c) 2020 Kian Cross
#

.PHONY: help
help:
	@echo "Commands:"
	@echo "    test           Run unit tests"
	@echo "    style-check    Check code style using black"
	@echo "    fix-fix        Fix any code styling issues using black"
	@echo "    types          Check types"

.PHONY: test
test:
	poetry run pytest --cov=pixy --cov-report=term-missing tests

.PHONY: style-check
style-check:
	poetry run black --check .

.PHONY: style-fix
style-fix:
	poetry run black .

.PHONY: types
types:
	poetry run mypy --strict pixy
