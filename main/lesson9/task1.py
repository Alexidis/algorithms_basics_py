# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
import hashlib


# генерируем матрицу смежности для двунаправленного графа
def Rabim_karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) > len(subs), 'Полстрка длинее строки или ей'

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
    find_count = 0

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            find_count += 1
    return find_count


def main():
    s_1 = input('Введите строку: ')
    s_2 = input('Введите подстроку для поиска: ')
    find_count = Rabim_karp(s_1, s_2)
    print(f'В строке "{s_1}" подстрока "{s_2}" встречается {find_count} раз')


