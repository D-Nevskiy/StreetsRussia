from datetime import datetime

from core.constants.news import (ALLOWED_EXTENSIONS, LEN_CATEGORY_NAME,
                                 LEN_TITLE)
from core.mixins import DateTimeMixin
from core.validators import validate_size_file
from django.core.validators import FileExtensionValidator
from django.db import models
from events.models import City


class News(DateTimeMixin):
    """
    Модель для хранения информации о новостном материале.

    Attributes:
        title (str): Заголовок новости.
        category (ManyToManyField): Связь с категориями новости.
        description (str): Описание новости.
        link (str, optional): Ссылка на новость (необязательно).
        age_restriction (str, optional): Возрастные ограничения
        для новости (необязательно).
        created_at (DateTimeField): Дата и время создания новости.
        updated_at (DateTimeField): Дата и время последнего обновления новости.
    """
    title = models.CharField(max_length=LEN_TITLE, verbose_name='Заголовок')
    category = models.ManyToManyField('Category', verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey(
        City,
        related_name='news',
        on_delete=models.CASCADE,
        verbose_name='Город проведения',
        help_text='Выберите город'
    )
    created_at = models.DateTimeField(
        default=datetime.now,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Category(DateTimeMixin):
    """
    Модель для хранения категорий.

    Attributes:
        name (str): Наименование категории.
    """
    name = models.CharField(
        max_length=LEN_CATEGORY_NAME,
        unique=True,
        verbose_name='Наименование'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class GalleryNews(DateTimeMixin):
    """
    Модель, представляющая галерею для новостей.

    Атрибуты:
        - file (FileField): Файл для новостей.
        - news (ForeignKey): Связь с новостью
    """
    file = models.FileField(
        'Файл',
        upload_to='files_news/',
        help_text='Загрузите файл.',
        validators=[
            FileExtensionValidator(
                ALLOWED_EXTENSIONS),
            validate_size_file
        ]
    )
    news = models.ForeignKey(
        News,
        related_name='news_images',
        on_delete=models.CASCADE,
        verbose_name='Новость',
        help_text='Медиа-файлы, связанные с этой новостью'
    )

    class Meta:
        verbose_name = 'Галерея новости'
