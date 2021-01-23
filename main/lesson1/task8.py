# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def main():
    (a, b, c) = input('Введите три числа ').split()
    (a, b, c) = (float(a), float(b), float(c))
    avg = 0

    if a < b < c or c < b <a:
        avg = b
    elif b < a < c or c < a < b:
        avg = a
    elif a < c < b or b < c <a:
        avg = c

    if avg:
        print(f'Медиана {avg[0]}')
    else:
        print(f'Медианы нет')
