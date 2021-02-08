# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

import sys

SIZE = 123


def version1():
    natural_num = SIZE
    odd_count = 0
    even_count = 0
    while natural_num:
        if natural_num % 2:
            odd_count += 1
        else:
            even_count += 1
        natural_num //= 10
    return natural_num, even_count, odd_count


def version2():
    natural_num = SIZE
    counter = [0, 0]
    while natural_num:
        if natural_num % 2:
            counter[0] += 1
        else:
            counter[1] += 1
        natural_num //= 10
    return natural_num, counter


def version3():
    natural_num = SIZE
    counter = {"odd": 0, "even": 0}
    while natural_num:
        if natural_num % 2:
            counter["odd"] += 1
        else:
            counter["even"] += 1
        natural_num //= 10
    return natural_num, natural_num, counter


def main():
    print(sys.version, sys.platform)
    ver = {'с переменными': list(version1()),
           'со списком': list(version2()),
           'с словарем': list(version3())
           }

    for k, v in ver.items():
        sizer = 0
        for att in v:
            sizer += sys.getsizeof(att)
        print(f'Версия {k} занимает {sizer}')

# версия с переменными лучше остальных
