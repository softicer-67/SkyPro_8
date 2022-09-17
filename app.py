import json
import re
from typing import Any


def check_names(text: dict) -> Any:
    for item in text:
        res = item['login']
        yield res


def main() -> None:
    with open('data.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    t = check_names(file)
    re_check(t)


def re_check(txt: str) -> Any:
    for item in txt:
        if re.match(r"^[A-Z]{1}", item):
            print(f'Login: {item} - Error - Первая буква не может быть заглавной')
        elif re.match(r"^\d+$", item):
            print(f'Login: {item} - Error - Логин не может состоять только из цифр')
        elif re.match(r"^[0-9]{1}.*", item):
            print(f'Login: {item} - Error - Первая буква не может быть цифрой')
        elif re.match(r".*[@$!%*#?&]{1}$", item):
            print(f'Login: {item} - Error - Последняя буква не может быть спецсимволом')
        elif re.match(r"^(?!.*\d).*$", item):
            print(f'Login: {item} - Error - В логине должна быть как минимум одна цифра')
        elif re.match(r"^(?!.*[A-Z]).*$", item):
            print(f'Login: {item} - Error - В логине должна быть как минимум одна заглавная буква')
        elif re.match(r"^(?!.*[@!$%*#?&]).*$", item):
            print(f'Login: {item} - Error - В логине должен быть как минимум один спецсимвол')
        else:
            print(True)


if __name__ == "__main__":
    main()
