#
import json


def load_candidates():
    """"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_all():
    """Эта функция покажет всех кандидатов"""
    return "\n\n".join(
        ["\n".join([candidate['name'], candidate['position'], candidate['skills']]) for candidate in load_candidates()])


def get_by_pk(pk):
    """Эта функция вернет кандидатов по <pk>"""
    for candidate in load_candidates():
        if candidate["pk"] == int(pk):
            url_pictures = candidate['picture']
            return f"<pre><img src='{url_pictures}'<pre>" \
                   f"<pre>{candidate['name']}\n" \
                   f"{candidate['position']}\n" \
                   f"{candidate['skills']}<pre>"


def get_by_skill(skill_name):
    """Эта функция вернет кандидатов по навыку"""
    candidates_list = ''
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower():
            candidates_list += "\n".join([candidate['name'], candidate['position'], candidate['skills']]) + "\n\n"
    return candidates_list
