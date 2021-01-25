# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

def main():
    (x1, y1) = input('Введите координаты первой точки ').split(' ')
    (x2, y2) = input('Введите координаты второй точки ').split(' ')
    (x1, y1) = (int(x1), int(y1))
    (x2, y2) = (int(x2), int(y2))

    if x1 == x2:
        print('Прямая не может быть проведена через данные точки')
    else:
        k = (y2 - y1) / (x1 - x2)
        b = (x2 * y1 - x1 * y2) / (x1 - x2)
        b_sign = '+' if b > 0 else '-'
        b_str = f'{b_sign} {abs(b)}' if b != 0 else ''
        equation = f'{k}x {b_str}'.strip()
        print(equation)
