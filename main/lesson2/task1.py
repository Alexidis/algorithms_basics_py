# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.


def main():
    while True:
        (a_str, sign, b_str) = input('Введите первое число знак и второе число ').split()
        if sign == '0':
            break
        elif sign not in ('0', '+', '-', '', '/'):
            print(f'Введеное вами значение {sign} не является знаком')
        elif sign == '/' and b_str == '0':
            print('Вы пытаетесь делить 0, я так не умею')
        else:
            a = float(a_str)
            b = float(b_str)
            if sign == '+':
                result = a + b
            elif sign == '-':
                result = a - b
            elif sign == '*':
                result = a * b
            else:
                result = a / b
            print(f'{a} {sign} {b} = {result}')
