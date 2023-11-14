import re
from datetime import datetime


def is_valid_email(email):
    """
    Проверяет, является ли email адрес действительным.
    :param email: Проверяемый email адрес.
    :return: True, если email действителен, иначе False.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    """
    Проверяет, является ли номер телефона действительным. Поддерживает несколько форматов:
    +79000000000, +7(800)0000000, и +7 900 000 00 00.
    :param phone: Проверяемый номер телефона.
    :return: True, если номер действителен, иначе False.
    """
    pattern = r"^\+7(\d{10}|\(\d{3}\)\d{7}|\s\d{3}\s\d{3}\s\d{2}\s\d{2})$"
    return re.match(pattern, phone) is not None


def is_valid_date(date):
    """
    Проверяет, является ли дата действительной. Поддерживает форматы DD.MM.YYYY и YYYY-MM-DD.
    :param date: Проверяемая дата.
    :return: True, если дата действительна, иначе False.
    """
    for fmt in ('%d.%m.%Y', '%Y-%m-%d'):
        try:
            datetime.strptime(date, fmt)
            return True
        except ValueError:
            pass
    return False


FORBIDDEN_WORDS = ['слово1', 'слово2', 'слово3']


def is_text(field):
    """
    Проверяет, является ли поле текстом и не содержит ли оно запрещенного содержания.
    :param field: Значение поля для проверки.
    :return: True, если поле является допустимым текстом, иначе False.
    """
    if field is not None and isinstance(field, str):
        min_length = 1  # Минимальная длина
        max_length = 255  # Максимальная длина

        if min_length <= len(field) <= max_length:
            if not contains_forbidden_content(field):
                return True
    return False


def contains_forbidden_content(text):
    """
    Проверяет, содержит ли текст запрещенные слова.
    :param text: Текст для проверки.
    :return: True, если найдено запрещенное содержание, иначе False.
    """
    for word in FORBIDDEN_WORDS:
        if re.search(word, text, re.IGNORECASE):
            return True
    return False
