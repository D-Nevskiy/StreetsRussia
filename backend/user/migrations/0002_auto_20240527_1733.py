# Generated by Django 3.2.18 on 2024-05-27 17:33

import core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='status',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[core.validators.validate_full_name], verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='passport_issue_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата выдачи паспорта'),
        ),
    ]
