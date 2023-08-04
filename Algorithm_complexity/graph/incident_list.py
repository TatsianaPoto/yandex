class Graph:
    def __init__(self):
        self.adj_list = {}  # Словарь для хранения списка инцидентности

    def add_vertex(self, vertex):
        # Добавление вершины в граф
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, weight=None):
        # Добавление ребра между вершинами u и v с возможной дополнительной информацией weight
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))  # Для неориентированного графа добавляем обратное ребро

    def remove_vertex(self, vertex):
        # Удаление вершины из графа
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for v in self.adj_list:
                self.adj_list[v] = [(u, w) for (u, w) in self.adj_list[v] if u != vertex]

    def remove_edge(self, u, v):
        # Удаление ребра между вершинами u и v
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u] = [(x, w) for (x, w) in self.adj_list[u] if x != v]
            self.adj_list[v] = [(x, w) for (x, w) in self.adj_list[v] if x != u]  # Для неориентированного графа удаляем обратное ребро

    def get_adjacent_edges(self, vertex):
        # Возвращает список инцидентных ребер для данной вершины
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            return []

    def get_all_vertices(self):
        # Возвращает список всех вершин в графе
        return list(self.adj_list.keys())

    def __str__(self):
        # Возвращает строковое представление списка инцидентности графа
        result = ""
        for vertex in self.adj_list:
            result += f"{vertex}: {self.adj_list[vertex]}\n"
        return result


# Пример использования:
if __name__ == "__main__":
    graph = Graph()

    # Добавление вершин в граф
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Добавление ребер между вершинами
    graph.add_edge("A", "B", 2)
    graph.add_edge("B", "C", 1)
    graph.add_edge("C", "D", 3)
    graph.add_edge("A", "D", 5)

    # Вывод списка инцидентности
    print(graph)
