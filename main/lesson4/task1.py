# 4. Определить, какое число в массиве встречается чаще всего.
import random
import cProfile

SIZE = 25000
array = [random.randint(0, SIZE) for _ in range(0, SIZE)]
# print(array)


def version1():
    common = {}
    recent = 0
    for item in array:
        common[item] = common.get(item, 0) + 1
    for key, value in common.items():
        if value > recent:
            recent = value
    recent_nums = [key for key, value in common.items() if value == recent]
    return recent_nums, recent
# 100
# 1000 loops, best of 5: 14 usec per loop
# 107 function calls in 0.000 seconds

# 500
# 1000 loops, best of 5: 71.8 usec per loop
# 507 function calls in 0.000 seconds

# 1000
# 1000 loops, best of 5: 145 usec per loop
# 1007 function calls in 0.000 seconds

# 10000
# 10007 function calls in 0.003 seconds

# 25000
# 25007 function calls in 0.007 seconds


def version2():
    array_set = list(set(array))
    result = {}

    for i in array_set:
        result[i] = 0

    for i in array:
        result[i] += 1

    max_count = 0
    max_item = ''

    for key, value in result.items():
        if value >= max_count:
            max_item = key
            max_count = value
    return max_item, max_count
# 100
# 1000 loops, best of 5: 12.9 usec per loop
# 5 function calls in 0.000 seconds

# 500
# 1000 loops, best of 5: 69.3 usec per loop
# 5 function calls in 0.000 seconds

# 1000
# 1000 loops, best of 5: 139 usec per loop
# 5 function calls in 0.000 seconds

# 10000
# 5 function calls in 0.002 seconds

# 25000
# 5 function calls in 0.005 seconds


def version3():
    SIZE = len(array)
    num = array[0]
    max_frq = 1
    for i in range(SIZE):
        frq = 1

        for k in range(i + 1, SIZE):
            if array[i] == array[k]:
                frq += 1

        if frq > max_frq:
            max_frq = frq
            num = array[i]
    return num, max_frq
# 100
# 1000 loops, best of 5: 311 usec per loop
# 5 function calls in 0.000 seconds

# 500
# 1000 loops, best of 5: 8.33 msec per loop
# 5 function calls in 0.010 seconds

# 1000
# 1000 loops, best of 5: 34 msec per loop
# 5 function calls in 0.036 seconds

# 10000
# 5 function calls in 3.602 seconds

# 25000
# 5 function calls in 22.686 seconds


cProfile.run('version1()')
cProfile.run('version2()')
cProfile.run('version3()')
