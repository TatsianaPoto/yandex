def find_shortest_path(n, cities, k, start, end):
    def can_travel_within_limit(city1, city2, limit):
        return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1]) <= limit

    queue = [(start, 0)]  # Очередь для BFS, каждый элемент - (город, количество дорог)
    visited = set([start])

    while queue:
        current_city, num_roads = queue.pop(0)

        if current_city == end:
            return num_roads

        for neighbor in range(1, n + 1):
            if neighbor not in visited and can_travel_within_limit(cities[current_city - 1], cities[neighbor - 1], k):
                queue.append((neighbor, num_roads + 1))
                visited.add(neighbor)

    return -1

if __name__ == "__main__":
    n = int(input())  # Количество городов
    cities = [tuple(map(int, input().split())) for _ in range(n)]  # Координаты городов

    k = int(input())  # Максимальное расстояние без дозаправки
    start, end = map(int, input().split())  # Начальный и конечный городы
