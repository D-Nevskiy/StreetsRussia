import uuid
from django.utils import timezone

from django.db import models


class BaseModel(models.Model):
    """
    Абстрактный базовый класс.

    Атрибуты:
        id (UUIDField): UUID модели.
        created_at (DateTimeField): Дата создания модели.
        updated_at (DateTimeField): Дата редактирования модели.


    Мета:
        abstract (bool): Абстрактная модель. (не создает записей в БД)

    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
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
