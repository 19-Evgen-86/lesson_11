import json
from typing import List, Union

from classes import Candidate, My_Exception


# загружает данные из json в переменную
def load_json(file_name) -> List[dict]:
    """
    загружает данные из JSON
    :param file_name:
    :return: List[dict]
    """
    with open(file_name, encoding='utf-8') as file:
        data: List[dict] = json.load(file)
    return data


# создает список объектов класса Candidate
def create_class_objects(data) -> List[Candidate]:
    """
    Cоздает список объектов класса Candidate
    :param data:
    :return:
    """
    candidates: List[Candidate] = []
    for item in data:
        candidates.append(Candidate(**item))
    return candidates


# возвращает одного кандидата по его id

def get_candidate_by_id(id_items: int, candidates: List[Candidate]) -> Union[Candidate, My_Exception]:
    """
    Возвращает список объектов класса Candidate, удовлетворяющих критерию поиска, либо My_Exception в случаи отсутствия
    результата
    :param id_items:
    :param candidates:
    :return: Union[Candidate, My_Exception]
    """
    for candidate in candidates:
        if candidate.id == id_items:
            return candidate
    else:
        raise My_Exception(" Кандидата с таким ID нет :( ")


def candidate_search(data: str, candidates: List[Candidate]) -> Union[List[Candidate], My_Exception]:
    """
    Возвращает список объектов класса Candidate, удовлетворяющих критерию поиска, либо My_Exception в случаи отсутствия
    результата
    :param data:
    :param candidates:
    :return: Union[List[Candidate], My_Exception]
    """
    result_search: List[Candidate] = []
    for candidate in candidates:
        if data.lower() in candidate.name.lower():
            result_search.append(candidate)
        if data.lower() in candidate.skills.lower():
            result_search.append(candidate)
    if result_search:
        return result_search
    else:
        raise My_Exception("Поиск не дал результатов! попробуйте уточнить критерий поиска!")
