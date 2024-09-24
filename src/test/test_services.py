import json
import logging
import pytest

# Подключение модуля для тестирования
from src.services_.services import analyze_cashback_categories


def test_analyze_cashback_categories():
    # Тестирование функции analyze_cashback_categories

    # Подготовка тестовых данных
    data = [
        {"date": "2022-05-15", "category": "Категория 1", "amount": 100},
        {"date": "2022-05-20", "category": "Категория 2", "amount": 200},
        {"date": "2022-05-25", "category": "Категория 1", "amount": 150},
        {"date": "2022-05-30", "category": "Категория 3", "amount": 300},
    ]
    year = 2022
    month = 5

    # Ожидаемый результат
    expected_result = {
        "Category 1": 25.0,
        "Category 2": 20.0,
        "Category 3": 30.0
    }

    # Вызов функции и проверка результата
    result = analyze_cashback_categories(data, year, month)
    assert result == expected_result
