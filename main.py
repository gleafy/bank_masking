"""
Модуль main.
Содержит основную логику взаимодействия с пользователем.
"""

from typing import Any, Dict, List, Optional

from src.csv_excel_reader import read_csv, read_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, search_by_description, sort_by_date
from src.utils import read_json
from src.widget import get_date, mask_account_card


def get_valid_input(prompt: str, valid_choices: Optional[list[str]] = None) -> str:
    """
    Запрашивает у пользователя ввод до тех пор, пока не будет введено корректное значение.

    :param prompt: Сообщение для пользователя.
    :param valid_choices: Список допустимых значений (если требуется проверка).
    :return: Корректный ввод пользователя.
    """
    while True:
        user_input = input(prompt).strip()
        if not valid_choices:
            if user_input:
                return user_input
            print("Ввод не может быть пустым.")
        else:
            lowered_choices = [choice.lower() for choice in valid_choices]
            if user_input.lower() in lowered_choices:
                return user_input
            # Определяем контекст по наличию "статус" в prompt
            if "статус" in prompt.lower():
                print(f'Статус операции "{user_input}" недоступен.\n')
                print(f"Доступные для фильтровки статусы: {', '.join(valid_choices)}")
            else:
                print(f'Выбран неверный вариант "{user_input}".')
                print(f"Доступные варианты: {', '.join(valid_choices)}")


def main() -> None:
    """
    Основная функция программы.
    Обеспечивает взаимодействие с пользователем и выполнение операций:
    - выбор источника данных (JSON/CSV/XLSX),
    - фильтрация по статусу,
    - сортировка по дате,
    - фильтрация по валюте (только рубли),
    - поиск по описанию,
    - вывод отформатированного списка транзакций.
    """
    print(
        """Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    # Выбор источника данных
    file_type = get_valid_input("Ваш выбор (1/2/3): ", ["1", "2", "3"])

    transactions: List[Dict[str, Any]] = []
    file_path = ""
    is_json = False  # Флаг для определения структуры данных
    try:
        if file_type == "1":
            file_path = "data/operations.json"
            transactions = read_json(file_path)
            is_json = True  # Устанавливаем флаг для JSON
            print("Для обработки выбран JSON-файл.")
        elif file_type == "2":
            file_path = "data/transactions.csv"
            transactions = read_csv(file_path)
            print("Для обработки выбран CSV-файл.")
        elif file_type == "3":
            file_path = "data/transactions_excel.xlsx"
            transactions = read_excel(file_path)
            print("Для обработки выбран XLSX-файл.")
    except FileNotFoundError:
        print(f"Ошибка: файл не найден по пути '{file_path}'.")
        return
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return

    if not transactions:
        print("Файл пуст или не удалось прочитать данные.")
        return

    # Фильтрация по статусу
    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
    print(f"Доступные для фильтровки статусы: {', '.join(valid_states)}")
    state = get_valid_input("Введите статус операции: ", valid_states).upper()
    filtered_transactions = filter_by_state(transactions, state)
    print(f'Операции отфильтрованы по статусу "{state}"')

    # Сортировка
    sort_choice = get_valid_input("\nОтсортировать операции по дате? (да/нет): ", ["да", "нет"]).lower()
    if sort_choice == "да":
        reverse_choice = get_valid_input(
            "Отсортировать по возрастанию или по убыванию? (возрастание/убывание): ", ["возрастание", "убывание"]
        ).lower()
        reverse = reverse_choice == "убывание"
        filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse)

    # Фильтрация по валюте (только рубли)
    currency_filter_choice = get_valid_input(
        "\nВыводить только рублевые транзакции? (да/нет): ", ["да", "нет"]
    ).lower()
    if currency_filter_choice == "да":
        # Фильтруем по-разному в зависимости от структуры
        if is_json:
            filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
        else:
            filtered_transactions = [t for t in filtered_transactions if t.get("currency_code") == "RUB"]
        print("Оставлены только рублевые операции.")

    # Поиск по описанию
    search_choice = get_valid_input(
        "\nОтфильтровать список транзакций по определенному слову в описании? (да/нет): ", ["да", "нет"]
    ).lower()
    if search_choice == "да":
        search_word = input("Введите слово для поиска в описании: ").strip()
        if search_word:
            filtered_transactions = search_by_description(filtered_transactions, search_word)
        else:
            print("Строка поиска пуста, дополнительная фильтрация по описанию не применялась.")

    # Вывод результатов
    if not filtered_transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")

        for t in filtered_transactions:
            # Дата
            date_formatted = get_date(t.get("date", ""))

            # Описание
            description = t.get("description", "")

            # Откуда -> Куда (с маскировкой)
            from_info = t.get("from")
            to_info = t.get("to")
            masked_from = mask_account_card(from_info) if from_info else None
            masked_to = mask_account_card(to_info) if to_info else None
            transfer_info = ""
            if masked_from and masked_to:
                transfer_info = f"{masked_from} -> {masked_to}"
            elif masked_to:
                transfer_info = masked_to

            amount = "N/A"
            currency_name = ""
            if is_json:
                op_amount_dict = t.get("operationAmount", {})
                amount = op_amount_dict.get("amount", "N/A")
                currency_name = op_amount_dict.get("currency", {}).get("name", "")
            else:
                amount = t.get("amount", "N/A")
                currency_name = t.get("currency_name", "")
            amount_info = f"Сумма: {amount} {currency_name}"

            # Вывод
            print(f"{date_formatted} {description}")
            if transfer_info:
                print(transfer_info)
            print(amount_info)
            print()


if __name__ == "__main__":
    main()
