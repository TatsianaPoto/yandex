import heapq

def dijkstra(graph, start):
    # Инициализация списка расстояний и очереди с приоритетом
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        # Извлечение вершины с минимальным текущим расстоянием
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущее расстояние больше сохраненного, пропускаем эту вершину
        if current_distance > distances[current_vertex]:
            continue

        # Обновление расстояний до соседних вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

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
