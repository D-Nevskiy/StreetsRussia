run_dev:
	docker compose -f infra/docker-compose.local.yaml up -d --build

stop_dev:
	docker compose -f infra/docker-compose.local.yaml down -v 

conf_backend:
	docker exec street_russia-backend python manage.py makemigrations news events user partners && \
	docker exec street_russia-backend python manage.py migrate && \
	docker exec street_russia-backend python manage.py collectstatic --noinput

create_test_data:
	docker cp ./event_mock_data.sql street_russia-db:/event_mock_data.sql && \
    docker exec street_russia-db psql -U postgres -d postgres -f event_mock_data.sql && \
	docker exec -it street_russia-db rm /event_mock_data.sql
