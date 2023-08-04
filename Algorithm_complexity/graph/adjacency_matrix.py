class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        # Добавление ребра между вершинами u и v с возможной дополнительной информацией weight
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # Для неориентированного графа добавляем обратное ребро

    def remove_edge(self, u, v):
        # Удаление ребра между вершинами u и v
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0  # Для неориентированного графа удаляем обратное ребро

    def get_adjacent_vertices(self, vertex):
        # Возвращает список инцидентных вершин для данной вершины
        if 0 <= vertex < self.num_vertices:
            return [i for i in range(self.num_vertices) if self.adj_matrix[vertex][i] > 0]
        else:
            return []

    def get_weight(self, u, v):
        # Возвращает вес ребра между вершинами u и v
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.adj_matrix[u][v]
        else:
            return 0

    def __str__(self):
        # Возвращает строковое представление матрицы смежности графа
        result = ""
        for row in self.adj_matrix:
            result += " ".join(str(x) for x in row) + "\n"
        return result


# Пример использования:
if __name__ == "__main__":
    num_vertices = 4
    graph = Graph(num_vertices)

    # Добавление ребер между вершинами
    graph.add_edge(0, 1, 2)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 3)
    graph.add_edge(0, 3, 5)

    # Вывод матрицы смежности
    print(graph)
