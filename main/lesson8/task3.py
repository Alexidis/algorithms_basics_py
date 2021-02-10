# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import random


def generate_graph(num_nodes):
    nodes = [i for i in range(num_nodes)]
    graph = dict.fromkeys(nodes)
    for key in graph:
        graph[key] = set(random.sample(nodes,random.randint(1, num_nodes)))
    return graph


def dfs(graph, start, visited=None):
    # при первом заходе в функцию создаем множество мосещенных вершин для стартовой вершины
    if visited is None:
        visited = set()
    # считаем что стартовая вершина теперь посещена
    visited.add(start)
    # обходим все связные узлы кроме уже посещеных
    for next in graph[start] - visited:
        # обход связаных узлов лочернего узла кроме посещеных ранее
        dfs(graph, next, visited)
    return visited


def main():
    SIZE = int(input('Введите количество вершин '))
    graph = generate_graph(SIZE)
    for key, val in graph.items():
        print(key, val)
    start = int(input('С какой начать обход '))
    print(f'результат обхода от вержины {start}     {dfs(graph, start)}')


