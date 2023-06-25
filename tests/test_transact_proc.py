import os
from utils.transact_proccessing import *


def test_extract(test_data_extract):
    """
    Проверка на правильность извлечения транзакций
    """
    data = [
        {
        "id": 509552992,
        "state": "EXECUTED",
        "date": "2019-04-19T12:02:30.129240",
        "operationAmount": {
            "amount": "81513.74",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Maestro 9171987821259925",
        "to": "МИР 2052809263194182"
        },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]
    extracted_data = exctract_data(test_data_extract)
    assert data == extracted_data, "Incorrect extraction"
    os.remove(test_data_extract)


def test_is_cleanup_executed(test_cleanup):
    """Проверка на оставление выполненных транзакций"""
    data = [
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]
    assert cleanup_data(test_cleanup, "EXECUTED") == data, "Incorrect cleanup"


def test_is_cleanup_canceled(test_cleanup):
    """Проверка на оставление отменённых транзакций"""
    data = [
        {
            "id": 509552992,
            "state": "CANCELED",
            "date": "2019-04-19T12:02:30.129240",
            "operationAmount": {
                "amount": "81513.74",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "to": "МИР 2052809263194182"
        }
    ]
    assert cleanup_data(test_cleanup, "CANCELED") == data, "Incorrect cleanup"


def test_is_cleanup(test_cleanup):
    """Общая проверка"""
    assert cleanup_data(test_cleanup, "") == [], "Incorrect cleanup"


def test_is_sorted(test_sort):
    """Проверка сортировки"""
    data = [
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        },
        {
            "id": 509552992,
            "state": "EXECUTED",
            "date": "2019-04-19T12:02:30.129240",
            "operationAmount": {
                "amount": "81513.74",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "to": "МИР 2052809263194182"
        },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        }
    ]
    assert sort_data(test_sort) == data, "Incorrect sort"


def test_is_hide_card(test_hide_card):
    """Проверка сокрытия номера карты"""
    assert hide_card_number(test_hide_card) == "Visa Gold 7756 67** **** 2839", f"Does not hide"


def test_is_hide_account(test_hide_account):
    """Проверка сокрытия номера счёта"""
    assert hide_account_number(test_hide_account) == "Счет **9453", "Does not hide"


def test_output(test_get_last):
    """Проверка результата"""
    pt1 = "29.09.2019 Перевод со счета на счет\nСчет **9637 -> Счет **4961\n45849.53 USD\n"
    pt2 = "23.11.2018 Перевод с карты на карту\nVisa Platinum 5355 13** **** 8236 -> Maestro 8045 76** **** 9061\n79428.73 USD\n"
    pt3 = "31.07.2018 Перевод организации\nMasterCard 8532 49** **** 2395 -> Счет **9420\n34380.08 USD"
    pt4 = "01.06.2019 Перевод с карты на счет\nМИР 8201 42** **** 6664 -> Счет **9956\n60888.63 руб.\n"
    pt5 = "28.12.2018 Открытие вклада\nСчет **2391\n49192.52 USD\n"
    data = f"{pt1}\n{pt4}\n{pt5}\n{pt2}\n{pt3}"
    assert get_last_transactions(sort_data(test_get_last)) == data, "Incorrect output"