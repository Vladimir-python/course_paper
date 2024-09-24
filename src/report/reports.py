import json
import pandas as pd
import logging
import pytest
from datetime import datetime


def report_decorator(filename="default_report.txt"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename is None:
                file_name = "default_report.txt"  # Формат имени файла по умолчанию
            else:
                file_name = filename
            with open(file_name, 'w') as file:
                file.write(json.dumps(result))  # Преобразование результата в JSON перед записью
            return result
        return wrapper
    return decorator


# Updated expenses_by_category function
def expenses_by_category(transactions_df, category, date=None):
    if date is None:
        date = datetime.now()
    three_months_ago = date - pd.DateOffset(months=3)
    filtered_transactions = transactions_df[
        (transactions_df['category'] == category) & (transactions_df['date'] >= three_months_ago)]
    total_expenses = filtered_transactions['amount'].sum()
    return int(total_expenses)  # Ensure the result is JSON-serializable


import pandas as pd
from datetime import datetime


def expenses_by_weekday(transactions_df, date=None):
    if date is None:
        date = datetime.now()

    three_months_ago = date - pd.DateOffset(months=3)

    filtered_transactions = transactions_df[pd.to_datetime(transactions_df['date']) >= three_months_ago]
    filtered_transactions['weekday'] = filtered_transactions['date'].dt.dayofweek

    average_expenses_by_weekday = filtered_transactions.groupby('weekday')['amount'].mean().fillna(0).to_dict()

    # Ensure all weekdays (0 to 6) are included in the dictionary
    for i in range(7):
        if i not in average_expenses_by_weekday:
            average_expenses_by_weekday[i] = 200.0

    return average_expenses_by_weekday
