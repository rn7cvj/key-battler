run:
	docker compose unpause api

stop:
	docker compose pause api

update:
	docker compose up -d --no-deps --build api
	docker compose exec -w /api api python -m alembic upgrade head

update-pkgs:
	docker compose exec -w /api api pip install -r requirements.txt

update-db:
	docker compose cp ./api/database api:/api
	docker compose exec -w /api api python -m alembic revision --autogenerate -m "$(name)"
	docker compose exec -w /api api python -m alembic upgrade head
	docker compose cp api:/api/migrations/versions ./api/migrations

update-api:
	docker compose cp ./api api:.

start:
	docker compose up --build -d