def dfs(graph, node, visited):
    """
    Рекурсивная функция поиска в глубину.

    Parameters:
        graph (dict): Словарь смежности графа.
        node (int): Текущая вершина для обхода.
        visited (list): Массив для отслеживания посещенных вершин.

    Returns:
        None
    """
    # Помечаем текущую вершину как посещенную
    visited[node] = True
    # Выводим текущую вершину (можно выполнить любые другие операции здесь)
    print(node, end=' ')

    # Обходим всех соседей текущей вершины
    for neighbor in graph[node]:
        # Если соседняя вершина не была посещена, вызываем DFS для нее
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    # Пример графа в виде списка смежности
    graph = {
        1: [2, 3],
        2: [1, 3, 4],
        3: [1, 2, 4],
        4: [2, 3, 5],
        5: [4]
    }

    # Количество вершин в графе
    n = len(graph)
    # Создаем массив для отслеживания посещенных вершин
    visited = [False] * (n + 1)

    # Вызываем DFS из вершины 1 (можно выбрать любую другую вершину)
    dfs(graph, 1, visited)
