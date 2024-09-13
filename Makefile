PY_VERSION := 3.12
VENV := venv
WEBAPP_PATH = webapp

VENV_PATH = $(WEBAPP_PATH)/$(VENV)

clean:
		rm -rf $(VENV_PATH)
		find . -type f -name '*.pyc' -delete

.PHONY: env
env:
		@if [ ! -d $(VENV_PATH) ] ; \
		then \
				echo "No Python Virtual Envionment found, Creating..."; \
				python$(PY_VERSION) -m venv $(VENV_PATH); \
				make install; \
		else \
				echo "Python Virtual Envionment founded!. No need to Create"; \
		fi

.PHONY: install
install: env
		./$(VENV_PATH)/bin/pip install -r $(WEBAPP_PATH)/requirements/dev.txt

# docker compose command shortcut
.PHONY: up
up:
		docker compose up

.PHONY: down
down:
		docker compose down --rmi local

.PHONY: freeze-prod
freeze-prod:
		./$(VENV_PATH)/bin/pip freeze > $(WEBAPP_PATH)/requirements/dev.txt

# for django
.PHONY: test
test:
		docker exec -it webapp bash -c "python3 -m pytest --ds=asiayo.settings tests/"
