import pytest

from classes import Candidate


@pytest.fixture
def json_test_data():
    test_json = {
        "id": 1,
        "name": "Adela Hendricks",
        "picture": "https://picsum.photos/200",
        "position": "Go разработчик",
        "gender": "female",
        "age": 40,
        "skills": "go, python"
    }
    return test_json


# экземпляр класса Candidat для тестов
@pytest.fixture
def test_class_object():
    candidate = Candidate({
        "id": 1,
        "name": "Adela Hendricks",
        "picture": "https://picsum.photos/200",
        "position": "Go разработчик",
        "gender": "female",
        "age": 40,
        "skills": "go, python"
    })
    return candidate


@pytest.fixture
def test_list_class_objects():
    res = []
    res.append(Candidate({
        "id": 1,
        "name": "Adela Hendricks",
        "picture": "https://picsum.photos/200",
        "position": "Go разработчик",
        "gender": "female",
        "age": 40,
        "skills": "go, python"
    }))
    return res


@pytest.fixture
def test_candidate_search_result():
    return [{
        "id": 1,
        "name": "Adela Hendricks",
        "picture": "https://picsum.photos/200",
        "position": "Go разработчик",
        "gender": "female",
        "age": 40,
        "skills": "go, python"
    }]
