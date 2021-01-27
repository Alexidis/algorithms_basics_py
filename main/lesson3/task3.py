# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random


def main():
    lst = [random.randint(-20, 33) for _ in range(0, 10)]
    print(lst)
    local_max = {'idx': 0, 'value': lst[0]}
    local_min = {'idx': 0, 'value': lst[0]}
    for i, item in enumerate(lst):
        if item > local_max['value']:
            local_max['idx'] = i
            local_max['value'] = item
        if item < local_min['value']:
            local_min['idx'] = i
            local_min['value'] = item
    lst[local_max['idx']] = local_min['value']
    lst[local_min['idx']] = local_max['value']
    print(f'Значение максимального элемента {local_max["value"]}, а его индекс {local_max["idx"]}')
    print(f'Значение минимального элемента {local_min["value"]}, а его индекс {local_min["idx"]}')
    print(lst)
