# Загрузка Flask и необходимых функций из файла utils.
from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

# Создание образа Flask
app = Flask(__name__)


@app.route("/")
def page_main():
    """Эта функция открывает страницу на которой отображены все кандидаты"""
    return f"<pre>{get_all()}<pre>"


@app.route("/candidate/<pk>")
def page_candidate(pk):
    """Эта функция открывает страницу по <PK>"""
    return f"<pre>{get_by_pk(pk)}<pre>"


@app.route("/skills/<skill>")
def page_skills(skill):
    """Эта функция открывает страницу с сортировкой кандидатов по <skill>"""
    return f"<pre>{get_by_skill(skill)}<pre>"


# Инициализируем файл main
if __name__ == '__main__':
    app.run()
