-include .env
arrancar:
	@PROJECT_DIR="./frontend/" && \
	cd "$$PROJECT_DIR" && \
	yarn > /dev/null 2>&1 && \
	cd -
	docker compose -f compose.desarrollo.yml up -d --build
  
bajar:
	docker compose -f compose.desarrollo.yml down

migrarbd:
	docker exec -it ${APP_NAME}_backend python manage.py makemigrations
	docker exec -it ${APP_NAME}_backend python manage.py migrate

superuser:
	docker exec -it ${APP_NAME}_backend python manage.py createsuperuser
	
test:
	docker exec -it ${APP_NAME}_backend python manage.py test

terminalbackend:
	docker exec -it ${APP_NAME}_backend /bin/bash

terminalfrontend:
	docker exec -it ${APP_NAME}_frontend /bin/bash

terminalpostgres:
	docker exec -it ${APP_NAME}_db /bin/bash

modelo:
	docker exec -it ${APP_NAME}_backend python manage.py graph_models -a -o static/modelo.png

bddelete:
	sudo rm -rf database/

help:
	@echo "Uso: "
	@echo " make [COMANDO]"
	@echo ""
	@echo "Descripción:"
	@echo "  Este Makefile proporciona comandos para la administración de la aplicación utilizando Docker Compose."
	@echo ""
	@echo "Comandos:"
	@echo "  arrancar            Inicia la aplicación."
	@echo "  bajar               Detiene y elimina los contenedores de Docker en ejecución."
	@echo "  migrarbd            Ejecuta las migraciones de la base de datos."
	@echo "  superuser           Ejecuta la creacion de un superusuario en la base de datos."
	@echo "  test                Ejecuta los tests de la aplicación."
	@echo "  terminalbackend     Abre una terminal interactiva en el contenedor del backend."
	@echo "  terminalfrontend    Abre una terminal interactiva en el contenedor del frontend."
	@echo "  terminalpostgres    Abre una terminal interactiva en el contenedor de PostgreSQL."
	@echo "  modelo              Genera un diagrama del modelo de la base de datos."
	@echo "  bddelete            Elimina la base de datos."
	@echo "  help                Muestra esta ayuda."