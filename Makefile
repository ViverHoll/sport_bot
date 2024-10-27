project_dir := .




# Make database migration
.PHONY: migration
migration:
	alembic revision --autogenerate -m "m"

# Apply database migrations
.PHONY: migrate
migrate:
	alembic upgrade head

# Run bot
.PHONY: run
run:
	python -m app


# Run bot in docker container
.PHONY: app-run
app-run:
	@docker-compose stop
	@docker-compose up -d --remove-orphans
