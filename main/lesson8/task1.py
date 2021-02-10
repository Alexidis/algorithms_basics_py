# 1. На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
import numpy as np


# генерируем матрицу смежности для двунаправленного графа
def generate_graph(vertex_count):
    graph = []
    for vertex in range(vertex_count):
        vertex_links = [1 if v != vertex else 0 for v in range(vertex_count)]
        graph.append(vertex_links)
    return graph


# подсчитываем сумму жлементов выше побочной диаганали, т.к. ниже буду только повторения
def upper_elements(matrix):
    local_sum = 0
    for i, row in enumerate(matrix):
        local_sum += sum([row[j] for j in range(i, len(row))])
    return local_sum


def main():
    friends_count = int(input('Введите количество друзей '))
    graph = generate_graph(friends_count)
    print(*graph, sep='\n')
    handshakes_count = upper_elements(graph)
    print(f'Количество рукопожатий между {friends_count} друзьями равно {handshakes_count}')
    # тоже самое только с numpy - получаем элементы выше и равные главной диагонали и вычитаем главную диагональ
    # хотя в нашем случаеэто не обязательно
    handshakes_count = np.triu(graph).sum() - np.trace(graph)
    print(f'Количество рукопожатий между {friends_count} друзьями numpy равно {handshakes_count}')


