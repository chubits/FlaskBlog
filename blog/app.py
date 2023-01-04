from flask import Flask, render_template


# создаём Flask app, в него передаём имя текущего файла (таковы правила для создания основного приложения);
# создаем index view: обрабатываем обращение на корень сайта, отдаём обычный текст;
# при помощи декоратора @app.route("/") указываем, что данный view должен быть использован для обработки запроса на /, то есть корень сайта (или index view).


app = Flask(__name__)


# Можно добавить переменные части в URL-адрес: string, int, float, path, uuid. Тогда функция будет получать variable_name в качестве аргумента ключевого слова.
# При желании можyj использовать конвертер, чтобы указать тип аргумента, например <converter:variable_name>.


@app.route('/') # <int:sity>
# def index(sity:int):
#     return f'Hello Web!, {sity}'
def index():
    return render_template('index.html')
