from tinydb import TinyDB
from validation import is_valid_email, is_valid_phone, is_valid_date, is_text

# Инициализация базы данных TinyDB
db = TinyDB('db.json')


def determine_field_type(value):
    """
    Определяет тип поля формы.
    :param value: Значение поля.
    :return: Определенный тип поля.
    """
    if is_valid_date(value):
        return 'date'
    elif is_valid_phone(value):
        return 'phone'
    elif is_valid_email(value):
        return 'email'
    elif is_text(value):
        return 'text'
    else:
        return None


def add_template(template_name, fields):
    """
    Добавляет новый шаблон формы в базу данных.
    :param template_name: Название шаблона формы.
    :param fields: Словарь полей и их типов.
    """
    template = {"name": template_name, "fields": fields}
    db.insert(template)


def match_template(form_data):
    """
    Сопоставляет данные формы с сохраненными шаблонами на основе типов полей.
    :param form_data: Словарь данных формы для сопоставления.
    :return: Кортеж (template_name, unmatched_fields),
             где unmatched_fields - это словарь несовпадающих полей.
    """
    form_data_types = {determine_field_type(value) for value in
                       form_data.values()}

    for template in db.all():
        template_types = set(template['fields'].values())
        if template_types.issubset(form_data_types):
            return template['name'], {}  # Возвращаем имя шаблона и пустой список

    unmatched_fields = {}
    for field, value in form_data.items():
        unmatched_fields[field] = determine_field_type(value)

    return None, unmatched_fields  # Возвращаем None для имени шаблона и типы данных для несовпадающих полей


if __name__ == '__main__':
    # Пример использования функции match_template
    template_fields = {
        "field1": "+78005553535",
        "field2": "email@gmail.com",
        "field3": "Test_text",
        "field4": "01.01.1998",
        "field5": "TEXT"
    }

    result = match_template(template_fields)
    print(result)

# template_name = "Customer"
# fields = {
# "customer_email": "email",
# "customer_phone": "phone",
# "order_date": "date"
# }

#    add_template(template_name, fields)
