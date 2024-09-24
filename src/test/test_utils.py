# test_utils.py
import pytest
from unittest.mock import patch, Mock
from src.main_page.utils import process_data, create_json_response, use_api


@pytest.fixture
def sample_data():
    return {'key': 'value'}


def test_process_data(sample_data):
    # Тестирование функции process_data
    processed_data = process_data(sample_data)
    assert processed_data == sample_data  # Пример теста


def test_create_json_response(sample_data):
    # Тестирование функции create_json_response
    json_response = create_json_response(sample_data)
    assert json_response == '{"key": "value"}'  # Пример теста


@patch('utils.requests.get')
def test_use_api(mock_get):
    # Тестирование функции use_api
    mock_get.return_value.json.return_value = {'key': 'value'}
    api_data = use_api()
    assert api_data == {'key': 'value'}  # Пример теста
