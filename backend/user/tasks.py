from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task(subject, message, recipient_list, html_message):
    send_mail(
        subject,
        message,
        'from@example.com',
        recipient_list,
        html_message=html_message,
        fail_silently=False,
    )
