import logging

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from download.celery import app

import time


@app.task
def sleep_task(second):
  time.sleep(second)
