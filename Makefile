SECRET_KEY := $(shell python -c "import os; print(os.urandom(32).hex())")

.PHONE: prepare
prepare:
	export SECRET_KEY=$(SECRET_KEY)
	envsubst < env-template > src/.env
	cd src; \
	python manage.py migrate; \
	python manage.py loaddata static/db_dump.json

.PHONE: run
run:
	cd src; \
	python manage.py runserver
