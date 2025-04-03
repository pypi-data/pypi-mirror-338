# Contains useful

.PHONY: pylint
pylint:
	@uv run -m pylint -j 4 src

.PHONY: mypy
mypy:
	@uv run -m mypy src

.PHONY: black
black:
	@uv run -m black --check src

.PHONY: pydocstyle
pydocstyle:
	@uv run -m pydocstyle src

.PHONY: pytest
pytest:
	@uv run pytest

.PHONY: build
build:
	@uv build

.PHONY: clean
clean:
	rm -f .coverage
	rm -f coverage.xml
	rm -f junit.xml
	rm -rf dist
	rm -rf build

.PHONY: cleanall
cleanall: clean
	rm -rf .mypy_cache
	rm -rf .pytest_cache

.PHONY:
validate: black pylint pydocstyle mypy pytest
