from uuid import uuid4

from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from user.tasks import send_email_task


class UserAccountManager(BaseUserManager):

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


class UserAccount(AbstractBaseUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        USER = "USER", "user"
        PARTICIPANT = "PARTICIPANT", "participant"
        ORGANIZER = "ORGANIZER", "organizer"
        SPONSOR = "SPONSOR", "sponsor"

    class Status(models.TextChoices):
        UNCONFIRMED = "UNCONFIRMED", "Unconfirmed"
        CONFIRMED = "CONFIRMED", "Confirmed"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.UNCONFIRMED
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=20)

    passport_series = models.CharField(max_length=10)
    passport_number = models.CharField(max_length=20)
    passport_issue_date = models.DateField(null=True)
    passport_issued_by = models.CharField(max_length=100)

    consent_to_rights = models.BooleanField(default=False)
    сonsent_to_processing = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

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
