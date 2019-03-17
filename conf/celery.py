import os

import celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")


app = celery.Celery(__name__)

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
