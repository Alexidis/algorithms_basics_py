# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def main():
    repeats_count = int(input('Сколько чисел вы хотите ввести '))
    sought_for = input('Какую цифру вы хотите найти ')
    sought_for_count = 0
    for i in range(repeats_count):
        number = input('Введите число ')
        for digit in number:
            if digit == sought_for:
                sought_for_count += 1

    print(f'Цифра {sought_for} в последовательности встречается {sought_for_count}')
