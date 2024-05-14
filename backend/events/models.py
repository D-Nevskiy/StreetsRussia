from django.db import models
from core.constants.events import (
    LEN_TITLE,
    LEN_DESCRIPTION,
    LEN_DISCTIPLINE,
    LEN_CITY,
    LEN_PLAN,
    LEN_TYPE_AREA,
    LEN_ADDRESS,
    CITY,
    DISCTIPLINE,
    TYPE_AREA
)


class Event(models.Model):
    picture = models.ImageField(
        'Картинка меропрития',
        upload_to='pictures_events/',
        blank=True,
        help_text='Выберите фотографию'
    )
    title = models.CharField(
        'Название мероприятия',
        max_length=LEN_TITLE,
        unique=True,
        help_text='Введите название мероприятия'
    )
    description = models.TextField(
        'Описание',
        max_length=LEN_DESCRIPTION,
        help_text='Введите описание мероприятия'
    )
    date = models.DateField(
        'Дата проведения',
        help_text='Введите дату мероприятия'
    )
    discipline_of_event = models.CharField(
        'Дисциплина',
        max_length=LEN_DISCTIPLINE,
        choices=DISCTIPLINE
    )
    type_of_area = models.CharField(
        'Тип площадки',
        max_length=LEN_TYPE_AREA,
        choices=TYPE_AREA
    )
    plan_of_event = models.CharField(
        'План мероприятия',
        max_length=LEN_PLAN
    )
    city = models.CharField(
        'Город проведения',
        max_length=LEN_CITY,
        choices=CITY
    )
    address = models.CharField(
        'Адрес площадки',
        max_length=LEN_ADDRESS
    )
    is_moderation = models.BooleanField(
        default=False
    )
    additional_fields = models.JSONField(
        'Дополнительные поля',
        blank=True,
        null=True,
        help_text='Дополнительные поля в формате JSON'
    )
    count_entrant = models.IntegerField(
        default=0
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.date}: {self.title} '
