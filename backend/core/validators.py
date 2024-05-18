from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError

from core.constants.events import MAX_FILE_SIZE


def validate_size_file(value):
    """
    Проверяет превышение размера файла.

    Параметры:
    value (file) - Файл

    Исключения:
    ValidationError: Возникает в случае превышения размера файла.
    """
    filesize = value.size

    if filesize > MAX_FILE_SIZE:
        raise ValidationError(
            f'Превышен максимальный размер файла - '
            f'{MAX_FILE_SIZE / (1024 * 1024)} MB'
        )


def validate_date(value):
    """
    Валидирует дату.

    Параметры:
    value (str) - Строка с датой

    Исключения:
    ValidationError: Возникает в если вводимая дата прошедшая.
    """
    if value < timezone.now().date():
        raise ValidationError(
            "Дата мероприятия не может быть прошедшей"
        )


class PhoneNumberValidator(validators.RegexValidator):
    regex = r'^(\+7|7|8)?[10]\d{10}$'
    message = (
        'Пожалуйста, введите правильный номер телефона'
    )
    flags = 0
