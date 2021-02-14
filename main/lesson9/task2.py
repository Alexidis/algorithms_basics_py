# 2. Закодируйте любую строку по алгоритму Хаффмана.
import heapq
from collections import Counter, namedtuple


# узед
class Node (namedtuple('Node', ['left', 'right'])):
    # обход узла
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


# лист
class Leaf (namedtuple('Leaf', ['char'])):
    # обход листа
    def walk(self, code, acc):
        # защита на случай если строка состоит из повторяющегося сивола
        code[self.char] = acc or '0'


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        # заполняем список узлов запоминаю частоту появления элемента
        h.append((freq, len(h), Leaf(ch)))
    # преобразуем список в очередь с приоритетом по частоте появления
    # это гарантирует что элементы с одинаковым весом будут стоять рядом
    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        # забираем из очереди два наиболее редко встречающихся элемента
        # переменные _count1, _count2 нужны для защиты от ошибки
        freq1, _count1,  left = heapq.heappop(h)
        freq2,  _count2, right = heapq.heappop(h)
        # суммируем их частоты и добавляем в очередь новый элемент
        # по сути строим дерево в обратную сторону
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1

    code = {}
    if h:
        # т.к. после предыдущего цикла у нас в массиве кортежей только один элемент (root),
        # то что бы получить его делаем распаковку
        [(_freq, _count, root)] = h
        # рекусрсивно обходим дерево собирая все узла
        root.walk(code, '')

    return code


def main():
    s = input('Введите строку ')
    # кодируем строку
    code = huffman_encode(s)
    # получаем расшмфпрвку в битовом варианте
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    # распечатываем символы и соответсвуюзие им коды
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)
