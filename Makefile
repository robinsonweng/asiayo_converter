PY_VERSION := 3.12
VENV := venv
WEBAPP_PATH = webapp

VENV_PATH = $(WEBAPP_PATH)/$(VENV)

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
	docker compose -f dev.yml up

.PHONY: down
down:
	docker compose -f dev.yml down --rmi local

.PHONY: freeze-dev
freeze-dev:
	./$(VENV_PATH)/bin/pip freeze > $(WEBAPP_PATH)/requirements/dev.txt

# for django
.PHONY: test
test:
	docker exec -it webapp sh -c "python3 manage.py test tests"

.PHONY: style
style:
	docker exec -it webapp sh -c "python3 -m flake8 ."

.PHONY: check
check:
	make test style

clean:
	rm -rf $(VENV_PATH)
	find . -type f -name '*.pyc' -delete
