# Generated by Django 3.2.18 on 2024-05-24 13:53

import core.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования записи')),
                ('content', models.TextField(verbose_name='Содержимое письма')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронный адрес')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, validators=[core.validators.validate_phone_number], verbose_name='Номер телефона отправителя')),
                ('consent_to_rights', models.BooleanField(verbose_name='Согласие с правилами')),
                ('сonsent_to_processing', models.BooleanField(verbose_name='Согласие на обработку данных')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратная связь',
                'ordering': ['-created_at'],
            },
        ),
    ]
