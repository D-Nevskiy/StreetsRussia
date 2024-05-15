from datetime import datetime

from django.db import models

from core.constants.news import (
    LEN_TITLE,
    LEN_AGE_RESTRICTION,
    LEN_CATEGORY_NAME,
    )


class News(models.Model):
    """
    Модель для хранения информации о новостном материале.

    Attributes:
        title (str): Заголовок новости.
        category (ManyToManyField): Связь с категориями новости.
        description (str): Описание новости.
        link (str, optional): Ссылка на новость (необязательно).
        age_restriction (str, optional): Возрастные ограничения для новости (необязательно).
        created_at (DateTimeField): Дата и время создания новости.
        updated_at (DateTimeField): Дата и время последнего обновления новости.
    """
    title = models.CharField(max_length=LEN_TITLE, verbose_name='Заголовок')
    category = models.ManyToManyField('Category', verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(blank=True, null=True, verbose_name='Ссылка')
    age_restriction = models.CharField(max_length=LEN_AGE_RESTRICTION,
                                       blank=True,
                                       null=True,
                                       verbose_name='Возрастные ограничения'
                                       )
    created_at = models.DateTimeField(default=datetime.now, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Category(models.Model):
    """
    Модель для хранения категорий.

    Attributes:
        name (str): Наименование категории.
    """
    name = models.CharField(max_length=LEN_CATEGORY_NAME, unique=True, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class NewsImage(models.Model):
    """
    Модель для хранения изображений для новостей.

    Attributes:
        news (ForeignKey): Внешний ключ для связи с новостью.
        image (ImageField): Поле для хранения изображения.
    """
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='news_images',
                             verbose_name='Новость'
                             )
    image = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='Изображение')

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
