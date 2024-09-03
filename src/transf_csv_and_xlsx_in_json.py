"""
В данном модуле функция для преобразования
файлов 'xlsx' и 'csv' в формат 'json'
с созданием новых файлов
"""

import json
from os import path

import pandas as pd

path_to_data = path.join(path.dirname(path.dirname(__file__)), "data/")


def read_csv_file(csv: pd.DataFrame, new_name: str = "transactions") -> str:
    """Конвертирует файл 'csv' в 'json' и сохраняем, затем считываем через функцию 'processing_json_file'"""
    filename_csv = input(
        "Вы можете поменять название файла [CSV] перед конвертацией в json."
        "\nЕсли не хотите менять название, нажмите на [Enter] "
    )
    if filename_csv:
        new_name = filename_csv
    new_file_name = path_to_data + new_name + "(from-csv).json"
    csv.to_json(new_file_name, orient="records", indent=4)
    with open(new_file_name, encoding="UTF-8") as transactions_file:
        transactions = json.load(transactions_file)
        res = json.dumps(transactions, indent=4)
        return res


def read_xlsx_file(xlsx: pd.DataFrame, new_name: str = "transactions") -> str:
    """Конвертирует файл 'xlsx' в 'json' и сохраняем, затем считываем через функцию 'processing_json_file'"""
    filename_xlsx = input(
        "Вы можете поменять название файла [XLSX] перед конвертацией в json."
        "\nЕсли не хотите менять название, нажмите на [Enter] "
    )
    if filename_xlsx:
        new_name = filename_xlsx
    new_file_name = path_to_data + new_name + "(from-xlsx).json"
    xlsx.to_json(new_file_name, orient="records", indent=4)
    with open(new_file_name, encoding="UTF-8") as transactions_file:
        transactions = json.load(transactions_file)
        res = json.dumps(transactions, indent=4)
        return res


if __name__ == "__main__":
    df_csv = pd.read_csv(path_to_data + "transactions.csv", delimiter=";", encoding="UTF-8")
    df_xlsx = pd.read_excel(path_to_data + "transactions_excel.xlsx")
    read_csv = read_csv_file(df_csv)
    read_xlsx = read_xlsx_file(df_xlsx)
    print(read_csv)
    print(read_xlsx)
