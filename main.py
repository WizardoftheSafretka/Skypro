import os

from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.transactions import read_transactions_csv, read_transactions_excel
from src.utils import get_list_dict_about_trans_json


def main() -> list[dict]:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""

    json_path = os.path.join(os.getcwd(), "data", "operations.json")
    csv_path = os.path.join(os.getcwd(), "data", "transactions.csv")
    xlsx_path = os.path.join(os.getcwd(), "data", "transactions_excel.xlsx")

    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
          Выберите необходимый пункт меню:
          1. Получить информацию о транзакциях из JSON-файла
          2. Получить информацию о транзакциях из CSV-файла
          3. Получить информацию о транзакциях из XLSX-файла"""
    )
    choice_type_file = input()
    if choice_type_file == "1":
        print("Для обработки выбран JSON-файл.")
        trans = get_list_dict_about_trans_json(json_path)
    elif choice_type_file == "2":
        print("Для обработки выбран CSV-файл.")
        trans = read_transactions_csv(csv_path)
    elif choice_type_file == "3":
        print("Для обработки выбран XLSX-файл.")
        trans = read_transactions_excel(xlsx_path)

    print(
        '''Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING'''
    )
    valid_status = ["EXECUTED", "CANCELED", "PENDING"]
    status = ""
    while status not in valid_status:
        status = input().upper()
        if status not in valid_status:
            print(f"Статус операции {status} недоступен.")
    filter_trans = filter_by_state(trans, status)
    print(f"Операции отфильтрованы по статусу {status}")

    print("Отсортировать операции по дате? Да/Нет")
    user_choice_sort = input().title()
    print("Отсортировать по возрастанию или по убыванию?")
    user_choice_reverse_order = input().lower()
    reverse_order = True
    if user_choice_reverse_order == "по возрастанию":
        reverse_order = False
    elif user_choice_reverse_order == "убыванию":
        reverse_order = True

    if user_choice_sort == "Да":
        filter_trans = sort_by_date(filter_trans, reverse_order)

    print("Выводить только рублевые транзакции? Да/Нет")
    rub_choice_user = input().title()
    if rub_choice_user == "Да":
        if "currency_code" in trans:
            filter_trans_rub = [trans for trans in filter_trans if trans["currency_code"] == "RUB"]
        else:
            filter_trans_rub = [
                trans for trans in filter_trans if trans["operationAmount"]["currency"]["code"] == "RUB"
            ]
    filter_trans = filter_trans_rub

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_choice_keyword = input().title()
    if user_choice_keyword == "Да":
        search_word = input("Введите ключевое слово: ")
        filter_trans = process_bank_search(filter_trans, search_word)

    print("Программа: Распечатываю итоговый список транзакций...")
    if not filter_trans:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    print(f"Программа: Всего банковских операций в выборке: {len(filter_trans)}")
    return filter_trans
