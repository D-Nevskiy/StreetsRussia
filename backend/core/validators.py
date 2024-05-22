import re

from core.constants.events import MAX_FILE_SIZE
from django.core.exceptions import ValidationError


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


def validate_phone_number(value):
    """
    Проверяет правильность введенного номера телефона.

    Параметры:
    value (str) - Номер телефона

    Исключения:
    ValidationError: Возникает в случае, если номер
    телефона не соответствует формату.
    """
    pattern = re.compile(r'^((\+7|7|8)+([0-9]){10})$')
    if not pattern.match(value):
        raise ValidationError('Пожалуйста, введите правильный номер телефона')


def validate_passport_series(value):
    """
    Проверяет правильность введенной серии паспорта.

    Параметры:
    value (str) - Серия паспорта

    Исключения:
    ValidationError: Возникает в случае, если серия
    паспорта не содержит 4 цифры.
    """
    pattern = re.compile(r'^\d{4}$')
    if not pattern.match(value):
        raise ValidationError('Серия паспорта должна содержать 4 цифры.')


def validate_passport_number(value):
    """
    Проверяет правильность введенного номера паспорта.

    Параметры:
    value (str) - Номер паспорта

    Исключения:
    ValidationError: Возникает в случае, если номер
    паспорта не содержит 6 цифр.
    """
    pattern = re.compile(r'^\d{6}$')
    if not pattern.match(value):
        raise ValidationError('Номер паспорта должен содержать 6 цифр.')


def validate_full_name(value):
    """
    Проверяет правильность введенного полного имени.

    Параметры:
    value (str) - Полное имя

    Исключения:
    ValidationError: Возникает в случае, если имя не
    соответствует заданному формату.
    """
    pattern = re.compile(r'^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$')
    if not pattern.match(value):
        raise ValidationError('Ошибка при вводе имени.')
