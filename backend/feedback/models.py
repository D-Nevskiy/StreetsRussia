from django.db import models

from core.mixins import DateTimeMixin
from user.models import UserAccount
from core.validators import validate_phone_number
from core.constants.user import LEN_PHONE_NUMBER


class Feedback(DateTimeMixin):
    """

    """
    user = models.ForeignKey(
        UserAccount,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    ip_address = models.GenericIPAddressField(
        'IP отправителя',
        blank=True,
        null=True
    )
    content = models.TextField(
        'Содержимое письма'
    )
    email = models.EmailField(
        'Электронный адрес'
    )
    phone_number = models.CharField(
        'Номер телефона отправителя',
        max_length=LEN_PHONE_NUMBER,
        validators=[validate_phone_number]
    )
    consent_to_rights = models.BooleanField(
        verbose_name='Согласие с правилами'
    )
    сonsent_to_processing = models.BooleanField(
        verbose_name='Согласие на обработку данных'
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_at']

    def __str__(self):
        return f'Письмо от {self.email}'
