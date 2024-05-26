from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from core.constants.user import (LEN_FIRST_NAME, LEN_GENDER, LEN_LAST_NAME,
                                 LEN_MIDDLE_NAME, LEN_PASSPORT_ISSUED_BY,
                                 LEN_PASSPORT_NUMBER, LEN_PASSPORT_SERIES,
                                 LEN_PHONE_NUMBER, LEN_ROLE)
from core.mixins import DateTimeMixin
from core.validators import (validate_full_name, validate_passport_number,
                             validate_passport_series, validate_phone_number)
from user.tasks import send_email_task


class UserAccountManager(BaseUserManager):
    """
    Кастомный менеджер для модели UserAccount,
    чтобы обрабатывать создание и подтверждение пользователей.

    Методы:
    create_superuser(email, password)
        Создает и возвращает суперпользователя с указанными email и паролем.

    create_user(email, password=None, **extra_fields)
        Создает и возвращает пользователя с указанными email и паролем.
        Дополнительные поля могут быть предоставлены через extra_fields.

    generate_temporary_password()
        Генерирует и возвращает случайный временный пароль для пользователя.

    send_temporary_password_email(email, temporary_password)
        Отправляет электронное письмо пользователю с предоставленным
        временным паролем.

    approve_user(user)
        Одобряет указанного пользователя, устанавливая временный пароль,
        обновляя статус пользователя на подтвержденный и отправляя
        электронное письмо с временным паролем.
    """
    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password
        )
        user.role = UserAccount.Role.ADMIN
        user.status = UserAccount.Status.CONFIRMED
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(
            email=email,
            status=UserAccount.Status.UNCONFIRMED,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def generate_temporary_password(self):
        return UserAccount.objects.make_random_password()

    def send_temporary_password_email(self, email, temporary_password):
        subject = 'Временный пароль.'
        context = {'temporary_password': temporary_password}
        html_message = render_to_string('temporary_password.html', context)
        plain_message = strip_tags(html_message)
        send_email_task.delay(
            subject,
            plain_message,
            [email],
            html_message=html_message
        )

    def approve_user(self, user):
        temporary_password = self.generate_temporary_password()
        user.set_password(temporary_password)
        user.status = UserAccount.Status.CONFIRMED
        user.save()
        self.send_temporary_password_email(user.email, temporary_password)


class UserAccount(AbstractBaseUser, DateTimeMixin):
    """
    Модель учетной записи пользователя.

    Атрибуты:
        role (CharField): Роль пользователя.
        status (CharField): Статус пользователя.
        first_name (CharField): Имя пользователя.
        last_name (CharField): Фамилия пользователя.
        middle_name (CharField): Отчество пользователя.
        gender (CharField): Пол пользователя.
        date_of_birth (Datetime): Дата рождения пользователя.
        phone_number (CharField): Номер телефона пользователя.
        email (EmailField): Электронная почта пользователя.
        city (CharField): Город пользователя.
        passport_series (CharField): Серия паспорта пользователя.
        passport_number (CharField): Номер паспорта пользователя.
        passport_issue_date (DateField): Дата выдачи паспорта.
        passport_issued_by (CharField): Орган, выдавший паспорт.
        consent_to_rights (CharField): Согласие пользователя на
        права, по умолчанию False.
        сonsent_to_processing (CharField): Согласие пользователя
        на обработку данных.
        USERNAME_FIELD (str): Поле, используемое для уникальной
        идентификации пользователя.
        REQUIRED_FIELDS (list): Дополнительные поля, обязательные
        при создании суперпользователя.
        objects (UserAccountManager): Менеджер модели UserAccount.
    """
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        USER = "USER", "user"
        REGIONAL_DIRECTOR = "REGIONAL_DIRECTOR", "regional_director"

    class Status(models.TextChoices):
        UNCONFIRMED = "UNCONFIRMED", "Unconfirmed"
        CONFIRMED = "CONFIRMED", "Confirmed"

    class Gender(models.TextChoices):
        MALE = "MALE", "male"
        FEMALE = "FEMALE", "female"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        verbose_name='Роль'
    )

    status = models.CharField(
        max_length=LEN_ROLE,
        choices=Status.choices,
        default=Status.UNCONFIRMED,
        verbose_name='Статус'
    )

    first_name = models.CharField(
        max_length=LEN_FIRST_NAME,
        validators=[validate_full_name],
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=LEN_LAST_NAME,
        validators=[validate_full_name],
        verbose_name='Фамилия'
    )
    middle_name = models.CharField(
        max_length=LEN_MIDDLE_NAME,
        validators=[validate_full_name],
        verbose_name='Отчество'
    )
    gender = models.CharField(
        max_length=LEN_GENDER,
        choices=Gender.choices,
        verbose_name='Пол'
    )
    date_of_birth = models.DateField(null=True, verbose_name='Дата рождения')
    phone_number = models.CharField(
        max_length=LEN_PHONE_NUMBER,
        unique=True,
        validators=[validate_phone_number],
        verbose_name='Телефон'
    )
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    city = models.CharField(max_length=20, verbose_name='Город')
    passport_series = models.CharField(
        max_length=LEN_PASSPORT_SERIES,
        validators=[validate_passport_series],
        verbose_name='Серия паспорта'
    )
    passport_number = models.CharField(
        max_length=LEN_PASSPORT_NUMBER,
        validators=[validate_passport_number],
        verbose_name='Номер паспорта'
    )
    passport_issue_date = models.DateField(
        null=True,
        verbose_name='Дата выдачи паспорта'
    )
    passport_issued_by = models.CharField(
        max_length=LEN_PASSPORT_ISSUED_BY,
        verbose_name='Кем выдан паспорт'
    )

    consent_to_rights = models.BooleanField(
        default=False,
        verbose_name='Согласие с правилами'
    )
    сonsent_to_processing = models.BooleanField(
        default=False,
        verbose_name='Согласие на обработку данных'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        return self.role == UserAccount.Role.ADMIN

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if not self.role or self.role is None:
            self.role = UserAccount.Role.USER
        return super().save(*args, **kwargs)

    @property
    def is_staff(self):
        return self.role == UserAccount.Role.ADMIN
