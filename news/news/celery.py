from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.CELERYBEAT_SCHEDULE = {
    "clean_votes": {
        "task": "news_api.tasks.reset_upvote",
        "schedule": crontab(hour="*/24"),
    }
}
