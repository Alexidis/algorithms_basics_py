# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def main():
    natural_num = int(input('Введите натуральное число '))
    odd_count = 0
    even_count = 0
    while natural_num != 0:

        if natural_num % 2:
            odd_count += 1
        else:
            even_count += 1
        natural_num //= 10
    print(f'В вашем числе {even_count} четных и {odd_count} нечетных чисел')
