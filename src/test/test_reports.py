import pytest
from datetime import datetime
from src.report.reports import report_decorator, expenses_by_category, expenses_by_weekday
import pandas as pd

# Тест для функции expenses_by_category
def test_expenses_by_category():
    # Подготовка тестовых данных
    transactions_df = pd.DataFrame({
        'date': ['2022-05-15', '2022-05-20', '2022-05-25', '2022-05-30'],
        'category': ['Category A', 'Category B', 'Category A', 'Category C'],
        'amount': [100, 200, 150, 300]
    })
    category = 'Category A'
    date = datetime(2022, 5, 30)

    # Convert the 'date' column to datetime format
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])

    result = expenses_by_category(transactions_df, category, date)
    assert result == 250  # Expected total expenses for 'Category A' on date 2022-05-30


# Тест для функции expenses_by_weekday
def test_expenses_by_weekday():
    # Подготовка тестовых данных
    transactions_df = pd.DataFrame({
        'date': ['2022-05-15', '2022-05-20', '2022-05-25', '2022-05-30'],
        'amount': [100, 200, 150, 300]
    })
    date = datetime(2022, 5, 30)

    # Convert the 'date' column to datetime format
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])

    result = expenses_by_weekday(transactions_df, date)
    assert result[5] == 200.0  # Expected average expenses on weekday 5 (Saturday)


# Запуск тестов
if __name__ == "__main__":
    pytest.main([__file__])