from django.core.validators import FileExtensionValidator
from django.db import models

from core.constants.events import (ALLOWED_EXTENSIONS, LEN_ADDRESS, LEN_CITY,
                                   LEN_DESCRIPTION, LEN_DISCTIPLINE, LEN_PLAN,
                                   LEN_TITLE, LEN_TYPE_AREA, TYPE_AREA)
from core.validators import validate_date, validate_size_file


class GalleryEvent(models.Model):
    """
    Модель, представляющая галерею для меропрития.

    Атрибуты:
        - file (FileField): Файл для меропрития.
        - event (ForeignKey): Связь с мероприятием

    Мета:
        verbose_name (str): Название модели в единственном числе.
    """
    file = models.FileField(
        'Файл',
        upload_to='files_events/',
        help_text='Загрузите файл.',
        validators=[
            FileExtensionValidator(
                ALLOWED_EXTENSIONS),
            validate_size_file

        ],

    )
    event = models.ForeignKey(
        'Event',
        related_name='gallery_events',
        on_delete=models.CASCADE,
        verbose_name='Мероприятие',
        help_text='Медиа-файлы, связанные с этим мероприятием'
    )

    class Meta:
        verbose_name = 'Галерея меропрития'


class Discipline(models.Model):
    """
    Модель, представляющая дисциплину уличного спорта.

    Атрибуты:
        - name (CharField): Название дисциплины.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.


    Методы:
        __str__(): Возвращает строковое представление дисциплины.
    """
    name = models.CharField(
        'Название дисциплины',
        max_length=LEN_DISCTIPLINE,
        db_index=True
    )

    class Meta:
        verbose_name = 'Дисциплина уличного спорта'
        verbose_name_plural = 'Дисциплины уличного спорта'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    """
    Модель, представляющая город.

    Атрибуты:
        - name (CharField): Название города.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.


    Методы:
        __str__(): Возвращает строковое представление города.
    """
    name = models.CharField(
        'Название города',
        max_length=LEN_CITY,
        db_index=True
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    """
    Модель, представляющая мероприятие.

    Атрибуты:
        title (CharField): Название мероприятия.
        description (TextField): Описание мероприятия.
        date (DateField): Дата проведения мероприятия.
        discipline_of_event (ForeignKey): Тип дисциплины мероприятия.
        type_of_area (CharField): Тип площадки мероприятия.
        plan_of_event (CharField): План мероприятия.
        city (ForeignKey): Город проведения мероприятия.
        address (CharField): Адрес площадки мероприятия.
        is_moderation (BooleanField): Флаг модерации мероприятия.
        organizers_contact (JSONField): Дополнительные поля в формате JSON.
        count_entrant (IntegerField): Количество участников мероприятия.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление мероприятия.
    """
    title = models.CharField(
        'Название мероприятия',
        max_length=LEN_TITLE,
        help_text='Введите название мероприятия'
    )
    description = models.TextField(
        'Описание',
        max_length=LEN_DESCRIPTION,
        help_text='Введите описание мероприятия'
    )
    date = models.DateField(
        'Дата проведения',
        help_text='Введите дату мероприятия',
        validators=[
            validate_date
        ]
    )
    discipline_of_event = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        verbose_name='Дисциплина уличного спорта',
        help_text='Выберите дисциплину уличного спорта'
    )
    type_of_area = models.CharField(
        'Тип площадки',
        max_length=LEN_TYPE_AREA,
        choices=TYPE_AREA,
        help_text='Выберите тип площадки'
    )
    plan_of_event = models.CharField(
        'План мероприятия',
        max_length=LEN_PLAN,
        help_text='Введите план мероприятия'
    )
    city = models.ForeignKey(
        City,
        related_name='events',
        on_delete=models.CASCADE,
        verbose_name='Город проведения',
        help_text='Выберите город'
    )
    address = models.CharField(
        'Адрес площадки',
        max_length=LEN_ADDRESS
    )
    is_moderation = models.BooleanField(
        default=False
    )
    organizers_contact = models.JSONField(
        'Связь с организатором',
        blank=True,
        null=True,
        help_text='Введите ссылку на связь с организаторами'
    )
    count_entrant = models.IntegerField(
        default=0
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.date}: {self.title} '
