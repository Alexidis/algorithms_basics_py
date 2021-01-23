# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

def main():
    p1 = input('Введите координаты первой точки ').split(' ')
    p2 = input('Введите координаты второй точки ').split(' ')
    (x1, y1) = (int(p1[0]), int(p1[1]))
    (x2, y2) = (int(p2[0]), int(p2[1]))

    x_coef = y1 - y2
    x_str = f'{x_coef}x' if x_coef != 0 else ''

    y_coef = x2 - x1
    y_sign = '+' if y_coef > 0 else '-'
    y_str = f'{y_sign} {abs(y_coef)}y' if y_coef != 0 else ''

    free_coef = x1 * y2 - x2 * y1
    free_sign = '+' if free_coef > 0 else '-'
    free_str = f'{free_sign} {abs(free_coef)}' if free_coef != 0 else ''

    equation = f'{x_str} {y_str} {free_str}'.strip()
    print(equation)
