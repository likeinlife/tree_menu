.PHONE: prepare
prepare:
	cd src; \
	python manage.py migrate; \
	python manage.py loaddata static/db_dump.json

.PHONE: run
run:
	cd src; \
	python manage.py runserver
