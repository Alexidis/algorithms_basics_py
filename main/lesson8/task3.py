# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


def generate_graph(vertex_count):
    graph = {}
    for vertex in range(vertex_count):
        graph[vertex] = {v for v in range(vertex_count) if v != vertex}
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
    SIZE = 5
    graph = generate_graph(SIZE)
    for key, val in graph.items():
        print(key, val)
    print(dfs(graph, 0))


