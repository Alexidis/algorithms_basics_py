# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random


def bubble_sort(array):
    array_len = len(array)
    for i in range(array_len - 1):
        for j in range(array_len - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def main():
    size = 10
    unsorted_array = [random.randint(-100, 99) for i in range(size)]
    print(unsorted_array)
    print(bubble_sort(unsorted_array))




