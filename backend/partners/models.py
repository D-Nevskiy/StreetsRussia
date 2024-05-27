from django.core.validators import FileExtensionValidator
from django.db import models

from core.constants.partners import (ALLOWED_EXTENSIONS_PART,
                                     LEN_DESCRIPTION_PART, LEN_NAME_PARTNER,
                                     LEN_TYPE_PARTNER, TYPE_PARTNER)


class Partner(models.Model):
    """
    Модель, представляющая партёра.

    Атрибуты:
        name (CharField): Название партнёра.
        image (ImageField): Изображение партнёра.
        description (TextField): Описание партёра.
        type (CharField): Тип партнёра.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление партнёра.
    """
    name = models.CharField(
        'Название партнёра',
        max_length=LEN_NAME_PARTNER,
        unique=True,
    )
    image = models.ImageField(
        'Изображение парнёра',
        upload_to='partners_images/',
        validators=[
            FileExtensionValidator(ALLOWED_EXTENSIONS_PART),
        ]
    )
    description = models.TextField(
        'Описание партёра',
        max_length=LEN_DESCRIPTION_PART,
    )
    type = models.CharField(
        'Тип партнёра',
        max_length=LEN_TYPE_PARTNER,
        choices=TYPE_PARTNER
    )

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'

    def __str__(self):
        return f'{self.name}'
