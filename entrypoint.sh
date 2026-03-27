#!/bin/bash

echo "** Starting Django make migrations"
python src/manage.py makemigrations --noinput --scriptable -v 2

echo "** Starting Django migrate"
python src/manage.py migrate

if [ "${DJANGO_SUPERUSER_PASSWORD:-""}" ]; then
  echo "** Starting Django create superuser"
  python src/manage.py createsuperuser --noinput --username admin --email "${DJANGO_SUPERUSER_EMAIL:-"admin@email.com"}"
fi


echo "Starting Django..."
exec python src/manage.py runserver 0.0.0.0:${APP_PORT:-8001} --noreload