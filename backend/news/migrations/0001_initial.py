# Generated by Django 3.2.18 on 2024-05-23 10:03

import datetime

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования записи')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ManyToManyField(to='news.Category', verbose_name='Категория')),
                ('city', models.ForeignKey(help_text='Выберите город', on_delete=django.db.models.deletion.CASCADE, related_name='news', to='events.city', verbose_name='Город проведения')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='GalleryNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования записи')),
                ('file', models.FileField(help_text='Загрузите файл.', upload_to='files_news/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv']), core.validators.validate_size_file], verbose_name='Файл')),
                ('news', models.ForeignKey(help_text='Медиа-файлы, связанные с этой новостью', on_delete=django.db.models.deletion.CASCADE, related_name='news_images', to='news.news', verbose_name='Новость')),
            ],
            options={
                'verbose_name': 'Галерея новости',
            },
        ),
    ]
