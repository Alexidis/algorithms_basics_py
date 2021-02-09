# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

# проверочный граф
graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def Dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    nodes = [{'node_num': 0, 'path': [], 'cost': float('inf')} for _ in range(length)]
    nodes[start]['cost'] = 0
    min_cost = 0
    while min_cost != float('inf'):
        is_visited[start] = True
        # жобавляем в конец пути текущую вершину, т.к. для самой себя она всегда будет последней
        nodes[start]['path'].append(start)
        nodes[start]['node_num'] = start
        for i, vertex in enumerate(graph[start]):
            # если вершина достижима и не посещена
            if vertex and not is_visited[i]:
                # если текщая стоимость больше чем движение от родителя до новой вершины
                if nodes[i]['cost'] > vertex + nodes[start]['cost']:
                    # обновляем стоимость
                    nodes[i]['cost'] = vertex + nodes[start]['cost']
                    # если проверяемая вершина не посещена, меняем ее путь на путь из родительской вершины
                    if not is_visited[i]:
                        nodes[i]['path'] = nodes[start]['path'].copy()

        min_cost = float('inf')
        for i in range(length):
            # находим не посещеную ноду с минимальной стоимостью
            if min_cost > nodes[i]['cost'] and not is_visited[i]:
                min_cost = nodes[i]['cost']
                start = i
    return nodes


def main():
    print(*graph, sep='\n')
    s = int(input('От какой вершины считать '))
    modes = Dijkstra(graph, s)
    for node in modes:
        print(f'Для вершины {node["node_num"]} цена составляет {node["cost"]}, а путь {node["path"]}')
