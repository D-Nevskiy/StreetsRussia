from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from core.constants.events import (ALLOWED_EXTENSIONS, LEN_ADDRESS,
                                   LEN_CITY_NAME, LEN_DESCRIPTION,
                                   LEN_DISCIPLINE_NAME, LEN_REGION_CODE,
                                   LEN_REGION_NAME, LEN_SUBDISCTIPLINE_NAME,
                                   LEN_TITLE, LEN_TYPE_AREA_NAME,
                                   LEN_TYPE_EVENT_NAME, TYPE_AREA)
from core.mixins import DateTimeMixin
from user.models import UserAccount


class GalleryEvent(DateTimeMixin):
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
            FileExtensionValidator(ALLOWED_EXTENSIONS),
        ]
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
        verbose_name_plural = 'Галерея меропритий'


class Discipline(DateTimeMixin):
    """
    Модель, представляющая дисциплину уличной культуры.

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
        max_length=LEN_DISCIPLINE_NAME,
    )

    class Meta:
        verbose_name = 'Дисциплина уличной культуры'
        verbose_name_plural = 'Дисциплины уличных культур'

    def __str__(self):
        return f'{self.name}'


class SubDiscipline(DateTimeMixin):
    """
    Модель, подкатегорию дисциплин.

    Атрибуты:
        - name (CharField): Название подкатегории.
        - discipline (ForeignKey): Дисциплины связанные с подкатегорией.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление субдицлиплины.
    """
    name = models.CharField(
        'Название подкатегории',
        max_length=LEN_SUBDISCTIPLINE_NAME
    )
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        related_name='sub_disciplines',
        verbose_name='Дисциплина'
    )

    class Meta:
        verbose_name = 'Подкатегория дисциплины'
        verbose_name_plural = 'Подкатегории дисциплин'

    def __str__(self):
        return f'{self.discipline.name} - {self.name}'


class Region(DateTimeMixin):
    """
    Модель, представляющая регион.

    Атрибуты:
        - name (CharField): Название региона.
        - owner (FokeignKey): Региональный руководитель.
        - code (CharField): Код региона.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление региона.
    """
    name = models.CharField(
        'Название региона',
        max_length=LEN_REGION_NAME,
        db_index=True,
        unique=True
    )
    owner = models.ForeignKey(
        UserAccount,
        related_name='regions',
        on_delete=models.CASCADE,
        verbose_name='Региональный руководитель',
    )
    code = models.CharField(
        'Код региона',
        max_length=LEN_REGION_CODE,
        unique=True
    )

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return f'{self.name}'


class TypeEvent(DateTimeMixin):
    """
    Модель, представляющая тип мероприятия.

    Атрибуты:
        - name (CharField): Название типа мероприятия.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление типа мероприятия.
    """
    name = models.CharField(
        'Название типа меропрития',
        max_length=LEN_TYPE_EVENT_NAME,
    )

    class Meta:
        verbose_name = 'Тип мероприятия'
        verbose_name_plural = 'Типы мероприятий'

    def __str__(self):
        return f'{self.name}'


class City(DateTimeMixin):
    """
    Модель, представляющая город.

    Атрибуты:
        - name (CharField): Название города.
        - region (ForeignKey): Название региона.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление города.
    """
    name = models.CharField(
        'Название города',
        max_length=LEN_CITY_NAME,
        db_index=True,
        unique=True
    )
    region = models.ForeignKey(
        'Region',
        on_delete=models.CASCADE,
        related_name='region_city',
        verbose_name='Регион',
        help_text='Выберите регион'
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class Location(DateTimeMixin):
    """
    Модель, представляющая локацию мероприятия.

    Атрибуты:
        region (ForeignKey): Регион проведения мероприятия.
        city (ForeignKey): Город проведения мероприятия.
        type_of_area (CharField): Тип площадки мероприятия.
        address (CharField): Адрес площадки мероприятия.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление локации.
        clean(): Валидирует город и регион на соответствие друг другу.
    """
    name = models.CharField(
        'Название площадки',
        max_length=LEN_TITLE,
        help_text='Введите название площадки',
    )
    region = models.ForeignKey(
        Region,
        related_name='location_region',
        on_delete=models.CASCADE,
        verbose_name='Регион проведения',
    )
    city = models.ForeignKey(
        City,
        related_name='location_city',
        on_delete=models.CASCADE,
        verbose_name='Город проведения',
        help_text='Выберите город'
    )
    type_of_area = models.CharField(
        'Тип площадки',
        max_length=LEN_TYPE_AREA_NAME,
        choices=TYPE_AREA,
        help_text='Выберите тип площадки'
    )
    address = models.CharField(
        'Адрес площадки',
        max_length=LEN_ADDRESS
    )

    class Meta:
        verbose_name = 'Локация мероприятия'
        verbose_name_plural = 'Локации мероприятия'

    def __str__(self):
        return f'{self.name}: {self.city.name}'

    def clean(self):
        if (self.region and self.city) and self.city != self.region.city:
            raise ValidationError(
                'Город должен принадлежать региону'
            )


class Event(DateTimeMixin):
    """
    Модель, представляющая мероприятие.

    Атрибуты:
        title (CharField): Название мероприятия.
        description (TextField): Описание мероприятия.
        start_datetime (DateTimeField): Дата и время начала мероприятия.
        end_datetime (DateTimeField): Дата и время окончания мероприятия.
        discipline (ForeignKey): Дисциплина мероприятия.
        sub_discipline (ForeignKey): Тип субдисциплины мероприятия.
        type_of_event (ForeignKey): Тип мероприятия.
        location (ForeignKey): Локация мероприятия.
        is_moderation (BooleanField): Флаг модерации мероприятия.
        organizers_contact (JSONField): Дополнительные поля в формате JSON.
        author (ForeignKey): Автор мероприятия.
        count_entrant (IntegerField): Количество участников мероприятия.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление мероприятия.
         clean(): Валидирует даты начала и конца мероприятия.
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
    start_datetime = models.DateTimeField(
        'Дата и время начала',
        help_text='Введите дату и время начала мероприятия'
    )
    end_datetime = models.DateTimeField(
        'Дата и время окончания',
        help_text='Введите дату и время окончания мероприятия'
    )
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.CASCADE,
        related_name='events_discipline',
        verbose_name='Дисциплина уличного спорта',
        help_text='Выберите дисциплину уличного спорта'
    )
    sub_discipline = models.ForeignKey(
        SubDiscipline,
        on_delete=models.CASCADE,
        related_name='events_sub_discipline',
        verbose_name='Субдисциплина уличного спорта',
        help_text='Выберите субдисциплину'
    )
    type_of_event = models.ForeignKey(
        TypeEvent,
        on_delete=models.CASCADE,
        related_name='events_type_of_event',
        verbose_name='Тип мероприятия',
        help_text='Выберите тип мероприятия'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='events_location',
        verbose_name='Локация мероприятия',
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
    author = models.ForeignKey(
        UserAccount,
        related_name='event_author',
        on_delete=models.CASCADE,
        verbose_name='Автор мероприятия',
    )
    count_entrant = models.IntegerField(
        default=0
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.location.region.name}: {self.title}'

    def clean(self):
        if self.start_datetime and self.end_datetime:
            if self.start_datetime >= self.end_datetime:
                raise ValidationError(
                    'Дата и время начала мероприятия должны быть '
                    'раньше даты и времени окончания.'
                )
            if self.start_datetime < timezone.now():
                raise ValidationError(
                    'Дата и время начала мероприятия не могут быть в прошлом.'
                )
