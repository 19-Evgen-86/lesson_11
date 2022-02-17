from unittest import mock
import pytest
import functions
from classes import My_Exception


@mock.patch('functions.create_class_objects')
def test_create_class_objects(mock_create_class_objects, json_test_data, test_class_object):
    mock_create_class_objects.return_value = test_class_object
    assert functions.create_class_objects(json_test_data) == test_class_object


@mock.patch('functions.candidate_search')
def test_candidate_search(mock_candidate_search, test_candidate_search_result):
    mock_candidate_search.return_value = test_candidate_search_result
    assert functions.candidate_search('Adela', test_candidate_search_result) == test_candidate_search_result


@mock.patch('functions.get_candidate_by_id')
def test_get_candidate_by_id(mock_get_candidate_by_id, test_candidate_search_result):
    mock_get_candidate_by_id.return_value = test_candidate_search_result
    assert functions.get_candidate_by_id(1, test_candidate_search_result) == test_candidate_search_result


def test_exception_ID(test_list_class_objects):
    with  pytest.raises(My_Exception):
        functions.get_candidate_by_id(2, test_list_class_objects)


def test_exception_name_or_skill(test_list_class_objects):
    with  pytest.raises(My_Exception):
        functions.candidate_search("Mikle", test_list_class_objects)
