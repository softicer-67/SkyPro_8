import json
import re
from typing import Any

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


# Достаем имена
def get_names(text: dict) -> Any:
    for item in text:
        res = item['login']
        yield res


# Старт программы, вызываем нужные функции
def main() -> None:
    with open('data.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    t = get_names(file)
    name_re_check(t)


# Проверка Regex всех возможных состояний
def name_re_check(txt: str) -> Any:
    for item in txt:
        error = f'{RED}Error{WHITE}'
        if re.match(r"^[A-Z]{1}", item):
            print(f'Login: {item} - {error} - Первая буква не может быть заглавной')
        elif re.match(r"^\d+$", item):
            print(f'Login: {item} - {error} - Логин не может состоять только из цифр')
        elif re.match(r"^[0-9]{1}.*", item):
            print(f'Login: {item} - {error} - Первая буква не может быть цифрой')
        elif re.match(r".*[@$!%*#?&]{1}$", item):
            print(f'Login: {item} - {error} - Последняя буква не может быть спецсимволом')
        elif re.match(r"^(?!.*\d).*$", item):
            print(f'Login: {item} - {error} - В логине должна быть как минимум одна цифра')
        elif re.match(r"^(?!.*[A-Z]).*$", item):
            print(f'Login: {item} - {error} - В логине должна быть как минимум одна заглавная буква')
        elif re.match(r"^(?!.*[@!$%*#?&]).*$", item):
            print(f'Login: {item} - {error} - В логине должен быть как минимум один спецсимвол')
        else:
            good = f'{GREEN}Good !{WHITE}'
            print(f'Login: {item} {good} Логин соответствует требованиям !')


if __name__ == "__main__":
    main()
