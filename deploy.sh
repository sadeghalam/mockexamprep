#!/bin/bash
# deploy.sh
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate
echo "Starting the app..."
exec gunicorn mockexamprep.wsgi:application --log-file -