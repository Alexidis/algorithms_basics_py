# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
from string import ascii_letters


def main():
    letter_idx = int(input('Введите номер буквы ')) - 1
    alphabet = ascii_letters[:26]
    result = alphabet[letter_idx]

    print(f'Под номером {letter_idx + 1} расположена буква {result}')
