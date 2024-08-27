"""
В данном модуле функция для преобразования
файлов 'xlsx' и 'csv' в формат 'json'
с созданием новых файлов
"""

import json
import pandas as pd


def get_csv_and_change_json(file_csv: pd.DataFrame, file_xlsx: pd.DataFrame) -> json:
    """Преобразовывает файлы csv и xlsx и создает json-файлы"""
    file_csv.to_json('data/csv_in_js.json', orient='records', indent=4)
    file_xlsx.to_json('data/xlsx_in_js.json', orient='records', indent=4)


if __name__ == '__main__':
    df_csv = pd.read_csv("data/transactions.csv", delimiter=';', encoding='UTF-8')
    df_xlsx = pd.read_excel("data/transactions_excel.xlsx")
    write_new_json_files = get_csv_and_change_json(df_csv, df_xlsx)
