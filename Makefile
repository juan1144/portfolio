SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --no-builtin-rules

VENV := .venv
PYTHON := $(VENV)/bin/python

.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help
	@grep -Eh '\s##\s' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ------------------:  ## dev env ------------------------------------------------------
dev:  ## Launch full dev environment (venv, install, db, migrate, run)
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		uv venv $(VENV); \
	fi
	@source $(VENV)/bin/activate && \
		uv pip install --project . && \
		docker compose up -d && \
		$(PYTHON) manage.py migrate && \
		$(PYTHON) manage.py runserver

# ------------------:  ## ruff ---------------------------------------------------------
ruff:  ## Check code with ruff
	ruff check --select I --fix
	ruff format
	ruff check

checkruff:  ## Check code with ruff
	ruff check --extend-select RUF100

formatruff:  ## Format code with ruff
	ruff format

# ------------------:  ## django -------------------------------------------------------
migrations:  ## Make migrations for all apps
	$(PYTHON) manage.py makemigrations

migrate:  ## Run migrations
	$(PYTHON) manage.py migrate

checkmigrations:  ## Check migrations without applying
	$(PYTHON) manage.py makemigrations --check --no-input --dry-run

superuser:  ## Create a superuser
	$(PYTHON) manage.py createsuperuser

run:  ## Run the Django server
	$(PYTHON) manage.py runserver

shell:  ## Start Django shell
	$(PYTHON) manage.py shell

collectmessages:  ## Extract messages to be translated
	$(PYTHON) manage.py makemessages -l es

compilessages:  ## Compile translations
	$(PYTHON) manage.py compilemessages -l es

collectstatic:  ## Collect static files for production
	$(PYTHON) manage.py collectstatic --noinput

clearcache:  ## Clear Django cache
	$(PYTHON) manage.py shell --command="from django.core.cache import cache; cache.clear()"

# ------------------:  ## docker -------------------------------------------------------
dockerup:  ## Start Docker services
	docker compose up -d

dockerstop:  ## Stop Docker services
	docker compose stop

# ------------------:  ## pre-commit ----------------------------------------------------
pcupdate:  ## Update pre-commit hooks
	pre-commit autoupdate

# ------------------:  ## tailwind ------------------------------------------------------
css:  ## Compile Tailwind CSS to base.css
	./tailwindcss -i static/css/input.css -o static/css/base.css
watch:  ## Start Tailwind watcher
	./tailwindcss -i static/css/input.css -o static/css/base.css --watch
