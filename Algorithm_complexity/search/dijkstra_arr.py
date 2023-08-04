def dijkstra(graph, start):
    # Инициализация списка расстояний
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    while True:
        # Находим вершину с минимальным текущим расстоянием
        min_distance = float('inf')
        min_vertex = None
        for vertex, distance in distances.items():
            if distance < min_distance:
                min_distance = distance
                min_vertex = vertex

        # Если текущее расстояние до всех вершин бесконечно, выходим из цикла
        if min_vertex is None:
            break

        # Обновляем расстояния до соседних вершин
        for neighbor, weight in graph[min_vertex].items():
            distance = min_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Помечаем текущую вершину как обработанную
        distances[min_vertex] = float('inf')

    return distances

# Пример графа в виде словаря смежности
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Начальная вершина
start_vertex = 'A'

# Вызов функции Дейкстры
result = dijkstra(graph, start_vertex)

# Вывод результатов
print("Кратчайшие расстояния от вершины", start_vertex, "до всех остальных вершин:")
for vertex, distance in result.items():
    print(f"{vertex}: {distance}")
