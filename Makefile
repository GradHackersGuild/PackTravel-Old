PYTHON = py # change the python run command according to your system
PIP = pip
PORT = 8080

.PHONY: help
help:
	@echo "Makefile for Django Project"
	@echo ""
	@echo "Usage:"
	@echo "  make setup        Install dependencies, apply migrations, and start the server"
	@echo "  make install      Install Django and dependencies"
	@echo "  make migrate      Apply migrations"
	@echo "  make run          Start the Django development server"
	@echo "  make tests         Run all tests"
	@echo ""

# Install Django and other dependencies
.PHONY: install
install:
	$(PIP) install -r requirements.txt
	$(PIP) install django django-allauth pymongo setuptools --upgrade


# Apply database migrations
.PHONY: migrate
migrate:
	$(PYTHON) manage.py migrate

# Start the Django server
.PHONY: run
run:
	$(PYTHON) manage.py runserver $(PORT)

# Install, migrate, and run server
.PHONY: setup
setup: install migrate run

# Run all django tests
.PHONY: tests
tests:
	$(PYTHON) manage.py test