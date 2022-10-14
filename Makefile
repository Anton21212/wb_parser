DOCKER_COMPOSE_FILE = "docker-compose.yml"
PROJECT_NAME = "wb_parser"

up:
# Создание и запуск контейнеров
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) up --build

up_d:
# Создание и запуск контейнеров в демоне
	docker-compose -p $(PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE) up --build -d

down:
# Остановить и удалить контейнеры, сети, образы и тома
	docker-compose -p $(PROJECT_NAME) down

stop:
# Остановить контейнеры
	docker-compose -p $(PROJECT_NAME) stop

image_prune:
# Удалить неиспользуемые образы
	printf"y\n" | docker image prune

container_prune:
# Удалить неиспользуемые контейнеры
	printf"y\n" | docker container prune