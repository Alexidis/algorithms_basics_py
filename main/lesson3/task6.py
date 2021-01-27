# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random


def main():
    lst = [random.randint(0, 80) for _ in range(0, 12)]
    print(lst)
    local_max = {'idx': 0, 'value': lst[0]}
    local_min = {'idx': 0, 'value': lst[0]}
    local_sum = 0
    for i, item in enumerate(lst):
        if item > local_max['value']:
            local_max['idx'] = i
            local_max['value'] = item
        if item < local_min['value']:
            local_min['idx'] = i
            local_min['value'] = item
    if local_max['idx'] > local_min['idx']:
        max_idx = local_max['idx']
        min_idx = local_min['idx'] + 1
    else:
        max_idx = local_min['idx']
        min_idx = local_max['idx'] + 1

    for i in range(min_idx, max_idx):
        local_sum += lst[i]
    print(f'Значение максимального элемента {local_max["value"]}, а его индекс {local_max["idx"]}')
    print(f'Значение минимального элемента {local_min["value"]}, а его индекс {local_min["idx"]}')
    print(f'Сумма элементов между минимальным и максимальным элментом {local_sum}')
