# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random


def main():
    matrix = [[random.randint(1, 10) for _ in range(6)] for _ in range(5)]
    for line in matrix:
        for item in  line:
            print(f'{item:>4}', end='')
        print()

    mins = [matrix[0][0]]
    for line in matrix:
        for i, item in enumerate(line):
            if len(mins) <= i:
                mins.append(item)
            elif item < mins[i]:
                mins[i] = item
    print(f'Минимумы по столбцам {mins}')

    local_max = 0
    for item in mins:
        if local_max < item:
            local_max = item
    print(f'Максимум среди минимумов {local_max}')
