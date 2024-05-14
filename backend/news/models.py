from django.db import models
from datetime import datetime


class News(models.Model):
    """
    Модель для хранения информации о новостном материале.
    """
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    category = models.ManyToManyField('Category', verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка')
    start_date = models.DateField(verbose_name='Дата начала', blank=True, null=True)
    end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    age_restriction = models.CharField(max_length=10,
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
    """
    name = models.CharField(max_length=50, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class NewsImage(models.Model):
    """
    Модель для хранения изображений для новостей.
    """
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Новость', related_name='images')
    image = models.ImageField(upload_to='image/', verbose_name='Изображение')

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
