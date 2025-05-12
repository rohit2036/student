# Makefile

IMAGE_NAME = one2n-api
TAG = 1.0.0
REGISTRY = yourdockerhubusername/$(IMAGE_NAME)

install:
	pip install -r requirements.txt

run:
	flask run

migrate:
	flask db init || true
	flask db migrate -m "Initial migration"
	flask db upgrade

test:
	python -m unittest discover tests

lint:
	flake8 app

docker-login:
	echo "$$DOCKER_PASSWORD" | docker login -u "$$DOCKER_USERNAME" --password-stdin

docker-build:
	docker build -t $(REGISTRY):$(TAG) .

docker-push:
	docker push $(REGISTRY):$(TAG)

all: install test lint docker-build docker-push

