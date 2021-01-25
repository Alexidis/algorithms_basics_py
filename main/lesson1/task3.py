# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
from random import randint
from string import ascii_letters


def main():
    random_type = input('Выберите тип случайного числа \n' +
                        '1 - целые числа\n' +
                        '2 - вещественные числа\n' +
                        '3 - буквы\n')
    if random_type == '1':
        borders = input('Введите границы для поиска случайного целого числа ').split(' ')
        left_border = int(borders[0])
        right_border = int(borders[1])
        int_left_borders = min(left_border, right_border)
        int_right_borders =  max(left_border, right_border)
        result = randint(int_left_borders, int_right_borders)
        print(f'Случайное целое число {result}')

    elif random_type == '2':
        max_round = 10 ** 5
        borders = input('Введите границы для поиска случайного вещественного числа ').split(' ')
        (left_border, right_border) = (float(min(borders)), float(max(borders)))
        # границы делим на целую часть и дробную
        left_tuple = divmod(left_border, 1)
        right_tuple = divmod(right_border, 1)

        left_border_int = int(left_tuple[0])
        right_border_int = int(right_tuple[0])

        # определяем случайное значение в интервале целых чисел
        int_result = randint(left_border_int, right_border_int)

        # в зависимости от того пришлось ли число на пограничное значение определяем, находим границы для остатка
        if int_result == left_border_int:
            left_modulo = int(round(left_tuple[1] * max_round, 0))
            right_modulo = max_round - 1
        elif int_result == right_border_int:
            left_modulo = 0
            right_modulo = int(round(left_tuple[1] * max_round, 0))
        else:
            left_modulo = 0
            right_modulo = max_round

        # определяем случайную часть остатка и переводим ее в вещественное число
        rand_modulo = randint(left_modulo, right_modulo) / max_round

        # получаем итоговый результат
        result = int_result + rand_modulo

        print(f'Случайное вещественное число {result}')
    elif random_type == '3':
        borders = input('Введите границы для поиска буквы алфавита ').split(' ')
        (left_border, right_border) = (min(borders), max(borders))
        alphabet = ascii_letters[:26]
        left_border_int = alphabet.index(left_border)
        right_border_int = alphabet.index(right_border)
        rand_idx = randint(left_border_int, right_border_int)
        result = alphabet[rand_idx]

        print(f'Случайная буква {result}')
