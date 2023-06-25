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
    keys = ['id', 'state', 'date', 'operationAmount', 'description']
    return [element for element in data if set(keys).issubset(set(element.keys())) and element["state"] == state]


def sort_data(data: list):
    """
    Сортирует транзакции по убыванию времени.
    :param data: список транзакций
    :return: отсортированный список транзакций
    """
    data_n = data[:]
    data_n.sort(key=lambda transact: transact['date'], reverse=True)
    return data_n


def hide_card_number(card: str):
    """
    Маскирует номер карты
    :param card: номер карты
    :return: замаскированный номер карты
    """
    card_data = card.split()
    card_data[-1] = f'{card_data[-1][:4]} {card_data[-1][4:6]}** **** {card_data[-1][-4:]}'
    result = ''
    for i in card_data:
        result += i + ' '
    return result[:-1]


def hide_account_number(account: str):
    """
    Маскирует номер счёта
    :param account: номер счёта
    :return: замаскированный номер счёта
    """
    return f'{account[:4]} **{account[-4:]}'


def get_last_transactions(data: list):
    """
    Получает и обрабатывает транзакции. Возвращает последние 5 операций.
    :param data: список транзакций
    :return: строку обработанных транзакций
    """
    result = ''
    data = data[:5]
    for transaction in data:
        transaction_str = ''
        transaction_str = f"{datetime.strptime(transaction['date'][:10], '%Y-%m-%d').strftime('%d.%m.%Y')}"
        transaction_str += f' {transaction["description"]}\n'
        summ = f'{transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}\n'
        if 'Счет' in transaction['to']:
            transaction['to'] = hide_account_number(transaction['to'])
        else:
            transaction['to'] = hide_card_number(transaction['to'])
        if 'from' in transaction.keys():
            if 'Счет' in transaction['from']:
                transaction['from'] = hide_account_number(transaction['from'])
            else:
                transaction['from'] = hide_card_number(transaction['from'])
            transaction_str += f'{transaction["from"]} -> {transaction["to"]}\n{summ}'
        else:
            transaction_str += f'{transaction["to"]}\n{summ}'
        result += transaction_str + '\n'
    return result[:-2]

