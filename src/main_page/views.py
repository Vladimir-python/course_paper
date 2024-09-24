import pandas as pd
from src.main_page.utils import *


def main_page_function(df):
    processed_data = process_data(df)
    json_response = create_json_response(processed_data)
    return json_response
