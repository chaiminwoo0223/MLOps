init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 scikit-learn pandas

server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi -f class3-mlflow-server minio/minio

dependency:
	make -C ../class1/ server

dependency-clean:
	make -C ../class1/ server-clean

all:
	make dependency
	make server

all-clean:
	make server-clean
	make dependency-clean