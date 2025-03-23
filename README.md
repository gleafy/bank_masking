# Банковский виджет маскировки

Проект представляет собой бэкенд-решение для виджета банковских операций клиента. В нём реализованы функции для маскировки номеров карт и счетов, форматирования дат, а также обработки списка банковских операций (фильтрация и сортировка). Проект разработан с использованием Poetry и соответствует критериям урока [sky.pro](https://sky.pro).

## Установка и использование

### Требования

- Python 3.13+
- [Poetry](https://python-poetry.org/)

### Шаги установки

1. **Клонируйте репозиторий с GitHub:**

   ```bash
   git clone <URL_вашего_репозитория>
   cd <название_папки_проекта>
   ```

2. **Установите зависимости с помощью Poetry:**

   ```bash
   poetry install
   ```

3. **Запустите проект:**

   Если у вас есть основной скрипт (например, `main.py`), выполните:
   
   ```bash
   poetry run python main.py
   ```

## Примеры использования

### Маскировка номера карты и счёта

Функции для маскировки реализованы в модуле `src/masks.py` и используются в модуле `src/widget.py`.

Пример работы функции `get_mask_card_number`:

```python
from src.masks import get_mask_card_number

card_number = 7000792289606361
print(get_mask_card_number(card_number))
# Вывод: "7000 79** **** 6361"
```

Пример работы функции `get_mask_account`:

```python
from src.masks import get_mask_account

account_number = 73654108430135874305
print(get_mask_account(account_number))
# Вывод: "**4305"
```

Пример работы функции `mask_account_card` из модуля `src/widget.py`:

```python
from src.widget import mask_account_card

# Для карты
print(mask_account_card("Visa Platinum 7000792289606361"))
# Вывод: "Visa Platinum 7000 79** **** 6361"

# Для счёта
print(mask_account_card("Счет 73654108430135874305"))
# Вывод: "Счет **4305"
```

### Форматирование даты

Функция `get_date` из модуля `src/widget.py` принимает строку с датой в формате ISO и возвращает её в формате "ДД.ММ.ГГГГ":

```python
from src.widget import get_date

iso_date = "2024-03-11T02:26:18.671407"
print(get_date(iso_date))
# Вывод: "11.03.2024"
```

### Фильтрация и сортировка банковских операций

Функции `filter_by_state` и `sort_by_date` реализованы в модуле `src/processing.py`.

Пример использования `filter_by_state`:

```python
from src.processing import filter_by_state

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]
executed_ops = filter_by_state(operations)
print(executed_ops)
# Вывод: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

Пример использования `sort_by_date`:

```python
from src.processing import sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
]
sorted_ops = sort_by_date(operations)
print(sorted_ops)
# Вывод: операции, отсортированные по дате (сначала самые новые)
```

### Работа с генераторами

Модуль `src/generators.py` содержит функции для работы с генераторами.

#### Фильтрация транзакций по валюте

Функция `filter_by_currency` возвращает итератор транзакций с заданной валютой:

```python
from src.generators import filter_by_currency

transactions = [
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    },
    {
        "operationAmount": {
            "currency": {"code": "EUR"}
        }
    },
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
# Вывод: транзакции с валютой "USD"
```

#### Получение описаний транзакций

Функция `transaction_descriptions` возвращает итератор описаний транзакций:

```python
from src.generators import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод со счета на счет"},
]

descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)
# Вывод: "Перевод организации", "Перевод со счета на счет"
```

#### Генерация номеров карт

Функция `card_number_generator` генерирует номера карт в заданном диапазоне:

```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
# Вывод:
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
# 0000 0000 0000 0005
```


## Тестирование

В проекте используется `pytest` для тестирования.  
Запуск тестов:
```bash
poetry run pytest
```

Для проверки покрытия кода тестами:
```bash
poetry run pytest --cov=src --cov-report=html
```

## Документация и ссылки

- **Документация проекта:**  
  Подробное описание функций содержится в докстрингах каждого модуля:
  - `src/masks.py`
  - `src/widget.py`
  - `src/processing.py`
  - `src/generators.py`

- **Инструменты и ресурсы:**  
  - [Poetry](https://python-poetry.org/)
  - [Black](https://github.com/psf/black)
  - [Flake8](https://flake8.pycqa.org/)
  - [isort](https://pycqa.github.io/isort/)
  - [mypy](https://mypy-lang.org/)
  - [sky.pro](https://sky.pro/)

## Лицензия

Данный проект не имеет лицензии.