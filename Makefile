SHELL:=/bin/bash
GREEN  := $(shell tput -Txterm setaf 2)

.PHONY: test-local
test-local: build-local
	@echo '${GREEN} waiting for grid'
	./wait-for-grid.sh;
	@echo '${GREEN} running all tests'
	pytest tests/ -s -v -n 3 --html=report.html --self-contained-html

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: build-local
build-local:
	docker-compose -f docker-compose.local.yml up -d

.PHONY: test-docker
test-docker:
	docker-compose -f docker-compose.yml up --build

.PHONY: teardown
teardown:
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.local.yml down

