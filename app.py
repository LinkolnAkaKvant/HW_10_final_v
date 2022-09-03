#
from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

#
app = Flask(__name__)


@app.route("/")
def page_main():
    """"""
    return f"<pre>{get_all()}<pre>"


@app.route("/candidate/<pk>")
def page_candidate(pk):
    """"""
    return f"<pre>{get_by_pk(pk)}<pre>"


@app.route("/skills/<skill>")
def page_skills(skill):
    """"""
    return f"<pre>{get_by_skill(skill)}<pre>"


#
if __name__ == '__main__':
    app.run()
