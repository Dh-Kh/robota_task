from celery.schedules import crontab
from dotenv import load_dotenv
import os

load_dotenv()

BROKER_URL = os.getenv("REDIS_URL")

CELERY_RESULT_BACKEND = os.getenv("REDIS_URL")

CELERYBEAT_SCHEDULE = {
    'task-name': {
        'task': 'tasks.container',
        'schedule': crontab(minute="0", hour="*"),
    },
}

CELERY_TIMEZONE = 'UTC'