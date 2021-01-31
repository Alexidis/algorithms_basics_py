# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

def main():
    repeats_count = int(input('Сколько чисел вы хотите ввести '))
    max_sum = 0
    max_num = ''
    for i in range(repeats_count):
        number = input('Введите число ')
        local_sum = 0
        for digit in number:
            local_sum += int(digit)
        if local_sum > max_sum:
            max_sum = local_sum
            max_num = number

    print(f'Число с наибольшей суммой {max_num}, а его сума равна {max_sum}')
