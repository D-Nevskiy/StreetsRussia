import logging

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@shared_task
def send_email_task(subject, message, recipient_list, html_message):
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
    except Exception as e:
        logger.error(f'ERROR: {e}')
        raise
