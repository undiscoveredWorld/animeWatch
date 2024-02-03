run-postgres:
	docker run -d -p 5431:5432 --rm \
		--env-file=docker.env \
		 --name=anime_watch_postgres_debug \
		 postgres:alpine
	docker run -d -p 8081:8080 --rm \
		--link anime_watch_postgres_debug \
		--name=anime_watch_adminer_degug  \
		adminer

stop-postgres:
	docker stop anime_watch_postgres_debug anime_watch_adminer_degug

run-mongo:
	docker run -d -p 27017:27017 --rm \
	--env-file=docker.env \
	--name=anime_watch_mongo_debug \
	mongo

	docker run -d -p 8082:8081 --rm \
	--env-file=docker.env \
	--env ME_CONFIG_MONGODB_URL=mongodb://backend:1G2a3M4e@anime_watch_mongo_debug \
	--name=anime_watch_mongo_express_debug \
	--link=anime_watch_mongo_debug \
	mongo-express

stop-mongo:
	- docker stop anime_watch_mongo_express_debug
	- docker stop anime_watch_mongo_debug

run:
	docker-compose up

build:
	docker-compose build

main:
	docker-compose build
	docker-compose up
