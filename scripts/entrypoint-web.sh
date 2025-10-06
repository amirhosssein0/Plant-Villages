#!/usr/bin/env bash
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput || true

if [ "${DEBUG}" = "False" ] || [ "${DEBUG}" = "0" ]; then
  exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120
else
  exec python manage.py runserver 0.0.0.0:8000
fi
