def bellman_ford(graph, start):
    # Инициализация списка расстояний
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Выполняем релаксацию V-1 раз, где V - количество вершин
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Проверяем наличие отрицательных циклов
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                # Обнаружен отрицательный цикл, возвращаем None
                return None

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

# Вызов функции Беллмана-Форда
result = bellman_ford(graph, start_vertex)

# Вывод результатов
if result is None:
    print("Обнаружен отрицательный цикл!")
else:
    print("Кратчайшие расстояния от вершины", start_vertex, "до всех остальных вершин:")
    for vertex, distance in result.items():
        print(f"{vertex}: {distance}")
