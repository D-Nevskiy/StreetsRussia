import uuid
from django.utils import timezone

from django.db import models


class DateTimeMixin(models.Model):
    """
    Миксин для включения полей created_at и updated_at в моделях.

    Атрибуты:
        created_at (DateTimeField): Дата создания записи.
        updated_at (DateTimeField): Дата редактирования записи.

    Мета:
        abstract (bool): Абстрактная модель. (не создает записей в БД)

    """
    created_at = models.DateTimeField(
        'Дата создания записи',
        default=timezone.now,
        editable=False
    )
    updated_at = models.DateTimeField(
        'Дата редактирования записи',
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    """
    Миксин для включения поля UUID в моделях.

    Атрибуты:
        id (UUIDField): UUID записи.

    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        abstract = True
