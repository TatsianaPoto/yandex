class Graph:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.inc_matrix = [[0 for _ in range(num_edges)] for _ in range(num_vertices)]

    def add_edge(self, u, v, edge_index):
        # Добавление ребра между вершинами u и v с указанием индекса ребра edge_index
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices and 0 <= edge_index < self.num_edges:
            self.inc_matrix[u][edge_index] = 1
            self.inc_matrix[v][edge_index] = -1

    def remove_edge(self, edge_index):
        # Удаление ребра с указанным индексом edge_index
        if 0 <= edge_index < self.num_edges:
            for i in range(self.num_vertices):
                if self.inc_matrix[i][edge_index] != 0:
                    self.inc_matrix[i][edge_index] = 0

    def get_adjacent_vertices(self, vertex):
        # Возвращает список инцидентных вершин для данной вершины
        if 0 <= vertex < self.num_vertices:
            return [i for i in range(self.num_edges) if self.inc_matrix[vertex][i] != 0]
        else:
            return []

    def __str__(self):
        # Возвращает строковое представление матрицы инцидентности графа
        result = ""
        for row in self.inc_matrix:
            result += " ".join(str(x) for x in row) + "\n"
        return result


# Пример использования:
if __name__ == "__main__":
    num_vertices = 4
    num_edges = 5
    graph = Graph(num_vertices, num_edges)

    # Добавление ребер между вершинами
    graph.add_edge(0, 1, 0)
    graph.add_edge(1, 2, 1)
    graph.add_edge(2, 3, 2)
    graph.add_edge(0, 3, 3)
    graph.add_edge(1, 3, 4)

    # Вывод матрицы инцидентности
    print(graph)
