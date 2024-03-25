#!/bin/sh

python manage.py makemigrations core

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn core.wsgi --bind 0.0.0.0:5000 --workers 1 --threads 1 --log-level debug