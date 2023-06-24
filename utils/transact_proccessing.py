from datetime import datetime
import json

def exctract_data(filename: str):
    """
    Читает список транзакций из файла и возвращает их.
    :param filename: название файла с данными
    :return: список транзакций
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def cleanup_data(data: list, state: str):
    """
    Оставляет в выборке транзакции только с нужным состоянием.
    :param data: список транзакций
    :param state: состояние транзакции
    :return: список транзакций
    """
    keys = ['id', 'state', 'date', 'operationAmount', 'description', 'from', 'to']
    return [element for element in data if set(keys) == set(element.keys()) and element["state"] == state]


def sort_data(data: list):
    """
    Сортирует транзакции по убыванию времени.
    :param data: список транзакций
    :return: отсортированный список транзакций
    """
    data_n = data[:]
    data_n.sort(key=lambda transact: transact['date'], reverse=True)
    return data_n
