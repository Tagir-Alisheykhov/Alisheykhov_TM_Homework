"""
В данном модуле функция для преобразования
файлов 'xlsx' и 'csv' в формат 'json'
с созданием новых файлов
"""

import json
from os import path
from typing import Any
import pandas as pd

file_csv = path.join(path.dirname(path.dirname(__file__)), "data/")
file_xlsx = path.join(path.dirname(path.dirname(__file__)), "data/")


def get_csv_and_change_json(csv: pd.DataFrame, xlsx: pd.DataFrame) -> Any:
    """Преобразовывает файлы csv и xlsx и создает json-файлы"""
    csv.to_json(file_csv + "csv_in_js.json", orient="records", indent=4)
    xlsx.to_json(file_xlsx + "xlsx_in_js.json", orient="records", indent=4)


if __name__ == "__main__":
    df_csv = pd.read_csv(file_csv + "transactions.csv", delimiter=";", encoding="UTF-8")
    df_xlsx = pd.read_excel(file_xlsx + "transactions_excel.xlsx")
    write_new_json_files = get_csv_and_change_json(df_csv, df_xlsx)
