#!/usr/bin/env bash
# ---
# Docker entrypoint script
# ---

set -eux;

# Collect static files
python manage.py collectstatic --noinput;

# Apply database migrations
python manage.py migrate;

# Start Gunicorn
gunicorn djazz.wsgi --bind=0.0.0.0:8000 --workers=4;