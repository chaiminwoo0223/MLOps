stream-server:
	docker compose -p class7-stream -f stream-docker-compose.yaml up -d

dashboard-server:
	docker compose -p class7-dashboard -f grafana-docker-compose.yaml up -d

stream-server-clean:
	docker compose -p class7-stream down -v
	docker rmi -f class7-stream-data-subscriber

dashboard-server-clean:
	docker compose -p class7-dashboard down -v
	docker rmi -f grafana/grafana

server:
	make stream-server
	make dashboard-server

server-clean:
	make stream-server-clean
	make dashboard-server-clean

dependency:
	make -C ../class1/ server
	make -C ../class5/ server
	make -C ../class6/ server

dependency-clean:
	make -C ../class6/ server-clean
	make -C ../class5/ server-clean
	make -C ../class1/ server-clean

all:
	make dependency
	make server

all-clean:
	make server-clean
	make dependency-clean

target-db-connection:
	PGPASSWORD=targetpassword psql -h localhost -p 5433 -U targetuser -d targetdatabase