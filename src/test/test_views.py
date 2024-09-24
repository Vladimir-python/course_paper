# test_views.py
import pandas as pd
import pytest
from unittest.mock import patch, Mock
from src.main_page.utils import process_data, create_json_response
from src.main_page.views import main_page_function


@pytest.fixture
def sample_data():
    return pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})


def test_process_data(sample_data):
    processed_data = process_data(sample_data)
    assert processed_data.equals(sample_data)  # Пример теста


def test_create_json_response(sample_data):
    json_response = create_json_response(sample_data)
    assert isinstance(json_response, str)  # Пример теста


@patch('utils.requests.get')
def test_use_api(mock_get):
    mock_get.return_value.json.return_value = {'key': 'value'}
    api_data = use_api()
    assert api_data == {'key': 'value'}  # Пример теста


@patch('utils.requests.get')
def test_main_page_function(sample_data, mock_get):
    mock_get.return_value.json.return_value = {'key': 'value'}
    json_response = main_page_function(sample_data)
    assert json_response == '{"A": [1, 2, 3], "B": [4, 5, 6]}'  # Пример теста

