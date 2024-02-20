init:
	pip install -U pip
	pip install "fastapi[all]"

main:
	uvicorn main:app --reload

crud-path:
	uvicorn crud_path:app --reload

crud-query:
	uvicorn crud_query:app --reload

crud-pydantic:
	uvicorn crud_pydantic:app --reload

server:
	docker build -t class4-api-server .
	docker run -d --name api-server -p 8000:8000 class4-api-server

server-clean:
	docker rm -f api-server
	docker rmi -f class4-api-server