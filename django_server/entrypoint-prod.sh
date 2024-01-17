#!/bin/bash

# Apply database migrations
 python manage.py migrate
python manage.py collectstatic

# Start the development server
gunicorn django_server.wsgi:application --bind 0.0.0.0:8000