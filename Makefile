# Makefile

# Variables
COMPOSE=docker-compose
WEB_SERVICE=web

# Commands
start:
	@$(COMPOSE) up -d

stop:
	@$(COMPOSE) down

runserver:
	@$(COMPOSE) exec $(WEB_SERVICE) python manage.py runserver 0.0.0.0:8000

build:
	@$(COMPOSE) up --build

remove:
	@$(COMPOSE) down --volumes

restart:
	@$(COMPOSE) down && $(COMPOSE) -d

makemigrations:
	@$(COMPOSE) exec $(WEB_SERVICE) python manage.py makemigrations

migrate:
	@$(COMPOSE) exec $(WEB_SERVICE) python manage.py migrate

createsuperuser:
	@$(COMPOSE) exec $(WEB_SERVICE) python manage.py createsuperuser

bash:
	@$(COMPOSE) exec $(WEB_SERVICE) bash

shell:
	@$(COMPOSE) exec $(WEB_SERVICE) python manage.py shell

collectstatic:
	@$(COMPOSE) exec $(WEB_SERVICE) python manage.py collectstatic --noinput

logs:
	@$(COMPOSE) logs -f

lint:
	@$(COMPOSE) exec $(WEB_SERVICE) flake8 apps
	@$(COMPOSE) exec $(WEB_SERVICE) black apps
	@$(COMPOSE) exec $(WEB_SERVICE) isort apps

install:
	@$(COMPOSE) exec $(WEB_SERVICE) pip install -r requirements.txt
	
# Help
help:
	@echo "Usage:"
	@echo "  make up                - Start the project with Docker Compose"
	@echo "  make stop              - Stop and remove Docker containers"
	@echo "  make restart           - Restart the project with Docker Compose (down and up)"
	@echo "  make makemigrations    - Create new Django migrations based on changes"
	@echo "  make migrate           - Apply Django database migrations"
	@echo "  make createsuperuser   - Create a Django superuser"
	@echo "  make bash              - Open a bash shell in the web container"
	@echo "  make shell             - Open the Django shell in the web container"
	@echo "  make logs              - Follow the logs of the containers"
	@echo "  make start             - Start the project in detached mode"
	@echo "  make remove            - Remove containers and volumes"
	@echo "  make runserver         - Run Django development server"
	@echo "  make logs              - Follow the logs of the containers"
	@echo "  make lint              - Lint the code with flake8, black and isort"
	@echo "  make install           - Install the project dependencies"