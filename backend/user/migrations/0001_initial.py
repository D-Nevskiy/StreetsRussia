# Generated by Django 3.2.18 on 2024-05-23 10:03

import core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования записи')),
                ('role', models.CharField(choices=[('ADMIN', 'admin'), ('USER', 'user'), ('REGIONAL_DIRECTOR', 'regional_director')], default='USER', max_length=20, verbose_name='Роль')),
                ('status', models.CharField(choices=[('UNCONFIRMED', 'Unconfirmed'), ('CONFIRMED', 'Confirmed')], default='UNCONFIRMED', max_length=20, verbose_name='Статус')),
                ('first_name', models.CharField(max_length=50, validators=[core.validators.validate_full_name], verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, validators=[core.validators.validate_full_name], verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=50, validators=[core.validators.validate_full_name], verbose_name='Отчество')),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=6, verbose_name='Пол')),
                ('date_of_birth', models.DateField(null=True, verbose_name='Дата рождения')),
                ('phone_number', models.CharField(max_length=12, unique=True, validators=[core.validators.validate_phone_number], verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('city', models.CharField(max_length=20, verbose_name='Город')),
                ('passport_series', models.CharField(max_length=4, validators=[core.validators.validate_passport_series], verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(max_length=6, validators=[core.validators.validate_passport_number], verbose_name='Номер паспорта')),
                ('passport_issue_date', models.DateField(null=True, verbose_name='Дата выдачи паспорта')),
                ('passport_issued_by', models.CharField(max_length=150, verbose_name='Кем выдан паспорт')),
                ('consent_to_rights', models.BooleanField(default=False, verbose_name='Согласие с правилами')),
                ('сonsent_to_processing', models.BooleanField(default=False, verbose_name='Согласие на обработку данных')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]