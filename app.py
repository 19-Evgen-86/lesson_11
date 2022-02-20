import os
from typing import List, Dict

from flask import Flask, render_template, url_for, request, Blueprint

import functions
from classes import My_Exception, PaginationHelper, Candidate

app = Flask(__name__)
# количестово записей отображаемых на странице
LIMIT = 10
# Путь у файлу JSON
JSON = os.path.join(app.root_path, "candidates.json")
# JSON = "candidates.json"


# загружаем данные из json
json_data: List[dict] = functions.load_json(JSON)
# создаем список кандидатов(экземпляры класса) из json
candidates: List[Candidate] = functions.create_class_objects(json_data)


@app.route('/', defaults={'page': 1})
@app.route('/<int:page>')
def all_candidates(page):
    # объект класса пагинации
    pagination: PaginationHelper = PaginationHelper(candidates, LIMIT)
    # результат, который будет передан пользователю
    result: List[Candidate] = pagination.items_page(page)

    return render_template("all_candidates_page.html", data=result, count_page=pagination.page_count())


@app.route('/my_page/')
def my_page():
    return render_template('my_page.html')


@app.route('/candidate/<int:id>')
def load_candidate_page(id):
    try:
        candidate: Candidate = functions.get_candidate_by_id(id, candidates)
        return render_template('candidate_page.html', data=candidate)
    except My_Exception as Exc:
        print(Exc)


@app.route('/search/<candidate_name>/', defaults={'page': 1})
@app.route("/search/<candidate_name>/<int:page>")
def load_candidates_by_name(candidate_name, page):
    result_search: List[Candidate] = functions.candidate_search(candidate_name, candidates)
    # объект класса пагинации
    pagination: PaginationHelper = PaginationHelper(result_search, LIMIT)
    # результат, который будет передан пользователю
    result: List[Candidate] = pagination.items_page(page)
    return render_template("all_candidates_page.html", data=result, count_candidates=str(len(result)),
                           count_page=pagination.page_count())


@app.route('/skill/<skill_name>/', defaults={'page': 1})
@app.route("/skill/<skill_name>/<int:page>")
def load_candidates_by_skills(skill_name, page):
    result_search = functions.candidate_search(skill_name, candidates)
    # объект класса пагинации
    pagination: PaginationHelper = PaginationHelper(result_search, LIMIT)
    # результат, который будет передан пользователю
    result: List[Candidate] = pagination.items_page(page)
    return render_template("all_candidates_page.html", data=result, count_candidates=str(len(result)), skill=skill_name,
                           count_page=pagination.page_count())


@app.route('/search/', defaults={'page': 1})
@app.route('/search/<int:page>', methods=['GET'])
def load_search_result(page):
    try:
        search_data: str = request.args.get('Search')
        result_search: List[Candidate] = functions.candidate_search(search_data, candidates)
        # объект класса пагинации
        pagination: PaginationHelper = PaginationHelper(result_search, LIMIT)
        # результат, который будет передан пользователю
        result: List[Candidate] = pagination.items_page(page)
        return render_template('all_candidates_page.html', data=result, count_candidates=str(len(result)),
                               count_page=pagination.page_count())

    except My_Exception as Exp:
        return render_template("errors.html", error=Exp)


if __name__ == '__main__':
    app.run()
