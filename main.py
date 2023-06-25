import utils.transact_proccessing as transact_proccessing
def main():
    """Вывод на экран ппоследних 5 выполненных транзакций"""
    data = transact_proccessing.exctract_data("operations.json")
    data = transact_proccessing.cleanup_data(data, "EXECUTED")
    data = transact_proccessing.sort_data(data)
    print(transact_proccessing.get_last_transactions(data))

if __name__ == "__main__":
    main()