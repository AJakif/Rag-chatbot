.PHONY: test install-dev

install-dev:
	pip install -e ".[test]"

test:
	python -m pytest tests/unit/test_health.py -v

run:
	uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8000