web: gunicorn --bind 0.0.0.0:$PORT nhs_reminder.wsgi
worker: celery -A nhs_reminder worker
