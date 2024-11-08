project_dir := .

# Make database migration
.PHONY: migration
migration:
	alembic revision \
	  --autogenerate
	  -m "init"

# Apply database migrations
.PHONY: migrate
migrate:
	alembic upgrade head

# Run bot
.PHONY: run
run:
	python -m app


# Build bot image
.PHONY: app-build
app-build:
	@docker-compose build

# Run bot database containers
.PHONY: app-run-db
app-run-db:
	docker-compose up -d --remove-orphans postgres redis

# Run bot in docker container
.PHONY: app-run
app-run:
	docker-compose stop
	docker-compose up -d --remove-orphans

# Stop docker containers
.PHONY: app-stop
app-stop:
	docker-compose stop

# Down docker containers
.PHONY: app-down
app-down:
	docker-compose down

# Destroy docker containers
.PHONY: app-destroy
app-destroy:
	docker-compose down -v --remove-orphans

# Show bot logs
.PHONY: app-logs
app-logs:
	docker-compose logs -f bot

# Drop all
.PHONY: app-drop
app-drop: app-destroy
	docker container prune -f
	docker images -q | xargs docker rmi -f
	docker volume prune -f