import logging

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


logger = logging.getLogger(__name__)


@shared_task
def send_email_task(subject, message, recipient_list, html_message):
    logger.info(f':::::::::::::::::::{settings.EMAIL_HOST}')
    logger.info(f':::::::::::::::::::{settings.EMAIL_PORT}')
    try:
        send_mail(
            subject,
            message,
            'anarant91@gmail.com',
            recipient_list,
            html_message=html_message,
            fail_silently=False,
        )
    except Exception as e:
        logger.error(f'ERROR: {e}')
        raise
