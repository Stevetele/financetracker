# your_project/celery.py
import os
from celery import Celery
from celery.schedules import crontab

app = Celery('phoneanceapp')
app.conf.beat_schedule = {
    'create-recurring-transactions-daily': {
        'task': 'finances.tasks.create_recurring_transactions',
        'schedule': crontab(minute=0, hour=0),  # Run the task every midnight
    },
}

# Set default Django settings for 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financetracker.settings')



# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
