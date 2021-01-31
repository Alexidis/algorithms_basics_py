# 4. Определить, какое число в массиве встречается чаще всего.
import random


def main():
    lst = [random.randint(0, 5) for _ in range(0, 10)]
    print(lst)
    common = {}
    recent = 0
    for item in lst:
        common[item] = common.get(item, 0) + 1
    for key, value in common.items():
        if value > recent:
            recent = value
    recent_nums = [key for key, value in common.items() if value == recent]
    print(f'Значения {recent_nums} встречаются {recent} раз(а)')
