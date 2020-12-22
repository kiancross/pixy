#
# Copyright (c) 2020 Kian Cross
#

.PHONY: help
help:
	@echo "Commands:"
	@echo "    test    Run unit tests"
	@echo "    lint    Lint code using black"

.PHONY: test
test:
	python3 -m unittest tests

.PHONY: lint
lint:
	black --check .
