.PHONE: lint
.PHONY: format

lint:
	flake8 .

format:
	black .