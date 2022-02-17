import json
from typing import List

from classes import Candidate, My_Exception


# загружает данные из json в переменную
def load_json(file_name):
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)
    return data


# создает список объектов класса Candidate
def create_class_objects(data):
    candidates = []
    for item in data:
        candidates.append(Candidate(item))
    return candidates


# возвращает одного кандидата по его id

def get_candidate_by_id(id: int, candidates: List[Candidate]):
    for candidate in candidates:
        if candidate.id == id:
            return candidate
    else:
        raise My_Exception(" Кандидата с таким ID нет :( ")


def candidate_search(data: str, candidates: List[Candidate]):
    result_search = []
    for candidate in candidates:
        if data.lower() in candidate.name.lower():
            result_search.append(candidate)
        if data.lower() in candidate.skills.lower():
            result_search.append(candidate)
    if result_search:
        return result_search
    else:
        raise My_Exception("Поиск не дал результатов! попробуйте уточнить критерий поиска!")
