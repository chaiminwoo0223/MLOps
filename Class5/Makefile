init:
	pip install -U pip
	pip install boto3==1.26.8 mlflow==1.30.0 "fastapi[all]" pandas scikit-learn

app:
	uvicorn app:app --reload

server:
	docker compose up -d

server-clean:
	docker compose down -v
	docker rmi -f class5-api-with-model

dependency:
	make -C ../class1/ server
	sleep 100
	make -C ../class3/ server
	python ../class3/save_model_to_registry.py

dependency-clean:
	make -C ../class3/ server-clean
	make -C ../class1/ server-clean

all:
	make dependency
	make server

all-clean:
	make server-clean
	make dependency-clean