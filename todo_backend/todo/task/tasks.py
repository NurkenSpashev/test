from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.core.mail import send_mail


@shared_task
def add():
    print('Request')
    pass


@shared_task
def send_message(email: str, task):
    print('Request')

    subject = "Sending an email with Django"
    message = f"Dear, {email}, task {task.title} was updated."
    send_mail(subject, message, 's.nurken92@gmail.com', [email])

    return email
