# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.


def main():
    year = int(input('Введите год '))
    if year % 4:
        print('Год не високосный')
    else:
        print('Год високосный')
