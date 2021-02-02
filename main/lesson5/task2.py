# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque


hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
       '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

unhex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
         9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def hex_sum(syllable1, syllable2):
    f = deque(syllable1)
    s = deque(syllable2)
    remainder = 0
    res = ''
    while f or s:
        f_digit = f.pop() if f else '0'
        s_digit = s.pop() if s else '0'
        (remainder, ceil) = divmod(hex[f_digit] + hex[s_digit] + remainder, 16)
        res = unhex[ceil] + res
    if remainder:
        res = unhex[remainder] + res
    return res


def hex_mul(syllable1, syllable2):
    f = list(syllable1)
    s = list(syllable2)
    f.reverse()
    s.reverse()

    res = ''
    for i, f_digit in enumerate(s):
        remainder = 0
        spam = ''
        for s_digit in f:
            (remainder, ceil) = divmod(hex[f_digit] * hex[s_digit] + remainder, 16)
            spam = unhex[ceil] + spam
        if remainder:
            spam = unhex[remainder] + spam
        spam += '0' * i
        res = hex_sum(res, spam)
    return res


def main():
    f_num = input('Введите первое число ').lstrip('0')
    s_num = input('Введите первое число ').lstrip('0')
    print(f'{str(f_num)} + {str(s_num)} = {hex_sum(f_num, s_num)}')
    print(f'{str(f_num)} * {str(s_num)} = {hex_mul(f_num, s_num)}')

