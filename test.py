import unittest
import random
from faker import Faker
from app import app
from db import add_template

# Создание экземпляра Faker для генерации тестовых данных
fake = Faker()


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Настройка тестового клиента Flask
        self.app = app.test_client()
        self.app.testing = True

    def generate_random_data(self):
        """
        Генерирует случайные данные для различного числа полей. Каждое имя поля уникально.
        """
        data_types = ['phone', 'email', 'text', 'date']
        data = {}
        num_fields = random.randint(1,
                                    len(data_types))  # Случайное количество полей

        for _ in range(num_fields):
            field_type = random.choice(data_types)
            unique_field_name = f"{field_type}_{fake.unique.lexify('????')}"

            if field_type == 'phone':
                data[unique_field_name] = fake.phone_number()
            elif field_type == 'email':
                data[unique_field_name] = fake.email()
            elif field_type == 'text':
                data[unique_field_name] = fake.sentence()
            elif field_type == 'date':
                data[unique_field_name] = fake.date(
                    pattern="%d.%m.%Y") if random.choice(
                    [True, False]) else fake.date(pattern="%Y.%m.%d")

        return data

    def test_get_form_post(self):
        # Генерация случайных данных
        random_data = self.generate_random_data()

        # Добавление шаблона для тестирования с различными типами данных
        add_template('TestTemplate',
                     {field: field for field in random_data.keys()})

        # Отправка POST-запроса со сгенерированными случайными данными
        response = self.app.post('/get_form', data=random_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('TestTemplate', response.data.decode())


if __name__ == '__main__':
    unittest.main()
