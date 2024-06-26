# Generated by Django 3.2.18 on 2024-05-23 10:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название партнёра')),
                ('image', models.ImageField(upload_to='partners_images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])], verbose_name='Изображение парнёра')),
                ('description', models.TextField(max_length=10000, verbose_name='Описание партёра')),
                ('type', models.CharField(choices=[('GENERAL', 'Генеральные'), ('STRATEGIC', 'Стратегические'), ('ORGANIZATIONAL', 'Организационные'), ('REGIONAL', 'Региональные')], max_length=100, verbose_name='Тип партнёра')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёры',
            },
        ),
    ]
