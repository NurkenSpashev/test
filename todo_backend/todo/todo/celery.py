from __future__ import absolute_import, unicode_literals
from django.conf import settings
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

app = Celery('todo')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(settings.INSTALLED_APPS)

