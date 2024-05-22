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


class PhoneNumberValidator(validators.RegexValidator):
    regex = r'^(\+7|7|8)?[10]\d{10}$'
    message = (
        'Пожалуйста, введите правильный номер телефона'
    )
    flags = 0


class PassportSeriesValidator(validators.RegexValidator):
    regex = r'^\d{4}$'
    message = 'Серия паспорта должна содержать 4 цифры.'
    flags = 0


class PassportNumberValidator(validators.RegexValidator):
    regex = r'^\d{6}$',
    message = "Номер паспорта должен содержать 6 цифр."
    flags = 0


class FullNameValidator(validators.RegexValidator):
    regex = r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$'
    message = "Ошибка при вводе имени."
    flags = 0
