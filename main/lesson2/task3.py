# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def main():
    asc_str = int(input('Введите натуральное число '))
    revers_str = ''

    while asc_str != 0:
        if revers_str or asc_str % 10:
            revers_str += str(asc_str % 10)
        asc_str //= 10
    print(f'Обратное число {revers_str}')
