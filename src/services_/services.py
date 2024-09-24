import json
from datetime import datetime
import logging



def analyze_cashback_categories(data, year, month):
    cashback_data = {}

    for transaction in data:
        transaction_date = datetime.strptime(transaction['date'], '%Y-%m-%d')
        if transaction_date.year == year and transaction_date.month == month:
            category = transaction['category']
            amount = transaction['amount']
            cashback = amount * 0.1  # Пример: 10% кешбэка от суммы транзакции
            # Заменяем кириллические названия категорий на латинские
            if category == "Категория 1":
                category = "Category 1"
            elif category == "Категория 2":
                category = "Category 2"
            elif category == "Категория 3":
                category = "Category 3"
            cashback_data[category] = cashback_data.get(category, 0) + cashback

    return cashback_data

# Пример данных для анализа (можно заменить на ваш набор данных)
data = [
    {"date": "2022-05-15", "category": "Категория 1", "amount": 100},
    {"date": "2022-05-20", "category": "Категория 2", "amount": 200},
    {"date": "2022-05-25", "category": "Категория 1", "amount": 150},
    {"date": "2022-05-30", "category": "Категория 3", "amount": 300},
]

year = 2022
month = 5

cashback_analysis = analyze_cashback_categories(data, year, month)
print(json.dumps(cashback_analysis, indent=2))
