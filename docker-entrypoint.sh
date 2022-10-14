#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py create_superuser_from_env
python manage.py runserver 0.0.0.0:80