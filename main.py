from src import masks


def main() -> None:

    # Пример номера карты и счета
    card = 7000792289606361
    account = 73654108430135874305
    # Получаем маскированные значения
    masked_card = masks.get_mask_card_number(card)
    masked_account = masks.get_mask_account(account)
    # Выводим результаты
    print("Маскированный номер карты:")
    print(masked_card)
    print("\nМаскированный номер счета:")
    print(masked_account)


if __name__ == "__main__":
    main()
