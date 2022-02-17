import os

from flask import Flask, render_template, url_for, request

import functions
from classes import My_Exception

JSON = os.path.join(os.path.pardir, "candidates.json")
app = Flask(__name__)

# загружаем данные из json
json_data = functions.load_json(JSON)
# создаем список кандидатов(экземпляры класса) из json
candidates = functions.create_class_objects(json_data)


@app.route('/')
def all_candidates():
    return render_template("all_candidates_page.html", data=candidates)


@app.route('/my_page/')
def my_page():
    return render_template('my_page.html')


@app.route('/candidate/<int:id>')
def load_candidate_page(id):
    try:
        candidate = functions.get_candidate_by_id(id, candidates)
        return render_template('candidate_page.html', data=candidate)
    except My_Exception as Exc:
        print(Exc)


@app.route("/search/<candidate_name>")
def load_candidates_by_name(candidate_name):
    result = functions.candidate_search(candidate_name, candidates)
    return render_template("all_candidates_page.html", data=result, count_candidates=str(len(result)))


@app.route("/skill/<skill_name>")
def load_candidates_by_skills(skill_name):
    result = functions.candidate_search(skill_name, candidates)
    return render_template("all_candidates_page.html", data=result, count_candidates=str(len(result)), skill=skill_name)


@app.route('/search/', methods=['GET'])
def load_search_result():
    try:
        search_data = request.args.get('Search')
        result_search = functions.candidate_search(search_data, candidates)
        return render_template('all_candidates_page.html', data=result_search)
    except My_Exception as Exp:
        return render_template("errors.html", error=Exp)


if __name__ == '__main__':
    app.run()
