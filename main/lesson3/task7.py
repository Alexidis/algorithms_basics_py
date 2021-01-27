# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
import random


def main():
    lst = [random.randint(1, 12) for _ in range(0, 10)]
    print(lst)
    local_min = {'idx': 0, 'value': lst[0]}
    local_min2 = {'idx': 0, 'value': lst[0]}
    for i, item in enumerate(lst):
        if item <= local_min['value']:
            local_min2 = local_min.copy()
            local_min['idx'] = i
            local_min['value'] = item
    print(f'Первый минимум {local_min["value"]} расположен под индексом {local_min["idx"]}')
    print(f'Второй минимум {local_min2["value"]} расположен под индексом {local_min2["idx"]}')
