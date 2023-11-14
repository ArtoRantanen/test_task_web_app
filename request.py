"""
Это тестовый модуль, к приложению можно обращаться через URL по форме:
/get_form?f_name1=email@gmail.com&f_name2=+78000004025&f_name3=sample_text
"""
import requests


def send_post_request(url, params):
    response = requests.post(url, data=params)
    return response


if __name__ == "__main__":
    url = "http://127.0.0.1:5000/get_form"
    data = {
        "field1": "+78005553535",
        "field2": "email@gmail.com",
        "field3": "Test_text",
        "field4": "01.01.1998",
        "field5": "TEXT"
    }

    response = send_post_request(url, data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    # template_name = "Customer"
    # fields = {
    # "customer_email": "email",
    # "customer_phone": "phone",
    # "order_date": "date"
    # }
    # data = {"template_name":"fields"}
    # response = send_post_request(url, data)
