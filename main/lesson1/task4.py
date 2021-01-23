# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
from string import ascii_letters


def main():
    (f_letter, s_letter) = input('Введите две буквы ').split(' ')
    alphabet = ascii_letters[:25]
    (f_letter_idx, s_letter_idx) = (alphabet.index(f_letter), alphabet.index(s_letter))
    dif = abs(f_letter_idx - s_letter_idx) - 1
    print(f'Между буквами {f_letter} и {s_letter} {dif} символов')
