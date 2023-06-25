import json
import pytest


@pytest.fixture
def test_data_extract():
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

    with open("test_file.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

    return "test_file.json"


@pytest.fixture
def test_cleanup():
    data = [
        {

        },
        {
            "id": 509552992
        },
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
    return data


@pytest.fixture
def test_sort():
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
    return data


@pytest.fixture
def test_hide_card():
    return "Visa Gold 7756673469642839"


@pytest.fixture
def test_hide_account():
    return "Счет 48943806953649539453"


@pytest.fixture
def test_get_last():
    data = [
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {
                "amount": "49192.52",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391"
        },
        {
            "id": 104807525,
            "state": "EXECUTED",
            "date": "2019-06-01T06:46:16.803326",
            "operationAmount": {
                "amount": "60888.63",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "МИР 8201420097886664",
            "to": "Счет 35116633516390079956"
        },
        {
            "id": 550607912,
            "state": "EXECUTED",
            "date": "2018-07-31T12:25:32.579413",
            "operationAmount": {
                "amount": "34380.08",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 8532498887072395",
            "to": "Счет 44238164562083919420"
        },
        {
            "id": 988276204,
            "state": "EXECUTED",
            "date": "2018-02-22T00:40:19.984219",
            "operationAmount": {
                "amount": "71771.90",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 4956649687637418",
            "to": "Счет 90562872508279542248"
        },
        {
            "id": 888407131,
            "state": "EXECUTED",
            "date": "2019-09-29T14:25:28.588059",
            "operationAmount": {
                "amount": "45849.53",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 35421428450077339637",
            "to": "Счет 46723050671868944961"
        },
        {
            "id": 634356296,
            "state": "EXECUTED",
            "date": "2018-01-21T01:10:28.317704",
            "operationAmount": {
                "amount": "96900.90",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 33407225454123927865",
            "to": "Счет 79619011266276091215"
        },
        {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {
                "amount": "79428.73",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061"
        }
    ]
    return data
