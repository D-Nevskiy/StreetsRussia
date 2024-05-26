from django.db import models

from core.constants.feedback import (LEN_NAME_FEEDBACK, LEN_PHONE_NUMBER,
                                     LEN_STATUS, STATUS_FEEDBACK)
from core.mixins import DateTimeMixin
from core.validators import validate_phone_number
from user.models import UserAccount


class Feedback(DateTimeMixin):
    """
    Модель, представляющая обратную связь.

    Атрибуты:
        - user (ForeignKey): Пользователь отправивший запрос.
        - name (CharField): Имя отправителя.
        - content (TextField): Содержимое письма
        - phone_number (BooleanField): Соглашение о правилах
        - consent_to_rights (BoolField): Номер телефона пользователя
        - сonsent_to_processing (BoolField): Номер телефона пользователя
        - status (CharField): Статус заявки.

    Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление обратной связи.
    """
    user = models.ForeignKey(
        UserAccount,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='feedback_user'
    )
    name = models.CharField(
        'Имя отправителя',
        max_length=LEN_NAME_FEEDBACK,
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
        validators=[validate_phone_number],
        null=True,
        blank=True
    )
    consent_to_rights = models.BooleanField(
        verbose_name='Согласие с правилами'
    )
    consent_to_processing = models.BooleanField(
        verbose_name='Согласие на обработку данных'
    )
    status = models.CharField(
        'Статус заявки',
        max_length=LEN_STATUS,
        choices=STATUS_FEEDBACK,
        default='PENDING'
    )

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_at']

    def __str__(self):
        return f'Письмо от {self.email}'


class FeedbackProcessing(DateTimeMixin):
    """
    Модель, представляющая обработку обратной связи.

    Атрибуты:
        - feedback (ForeignKey): Объект обратной связи.
        - text (TextField): Ответ на обратную связь
        - support_agent (ForeignKey): Объект агента поддержки.
        (отвечающий на сообщение)

        Мета:
        verbose_name (str): Название модели в единственном числе.
        verbose_name_plural (str): Название модели во множественном числе.

    Методы:
        __str__(): Возвращает строковое представление обработки обратной связи.

    """
    feedback = models.ForeignKey(
        Feedback,
        on_delete=models.CASCADE,
        related_name='feedback_processing'
    )
    text = models.TextField(
        'Тест ответа'
    )
    support_agent = models.ForeignKey(
        UserAccount,
        verbose_name='Агент поддержки',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Ответ на заявку'
        verbose_name_plural = 'Ответы на заявки'

    def __str__(self):
        return f'Ответ на заявку {self.feedback.email} ({self.feedback.name})'
