from flask import Flask, request, jsonify
from db import match_template, add_template as db_add_template

app = Flask(__name__)


@app.route('/get_form', methods=['GET', 'POST'])
def get_form():
    """
    Обрабатывает GET или POST запросы на получение формы.
    Извлекает данные из формы и сопоставляет с шаблонами.
    """
    if request.method == 'POST':
        form_data = request.form.to_dict()
    else:  # Если это GET запрос
        form_data = request.args.to_dict()

    template_name, unmatched_fields = match_template(form_data)

    if template_name:
        return jsonify({"template": template_name})
    else:
        return jsonify(unmatched_fields)


@app.route('/add_template', methods=['POST'])
def add_template_route():
    """
    Обрабатывает POST запросы на добавление нового шаблона.
    """
    data = request.json
    template_name = data.get("name")
    fields = data.get("fields")

    if not template_name or not fields:
        return jsonify({"error": "Необходимы название шаблона и поля"}), 400

    db_add_template(template_name, fields)
    return jsonify({"message": "Шаблон успешно добавлен"}), 201


if __name__ == '__main__':
    app.run(debug=True)
