class Graph:
    def __init__(self):
        self.adj_list = {}  # Словарь для хранения списка смежности

    def add_vertex(self, vertex):
        # Добавление вершины в граф
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        # Добавление ребра между вершинами u и v
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)  # Для неориентированного графа добавляем обратное ребро

    def remove_vertex(self, vertex):
        # Удаление вершины из графа
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for v in self.adj_list:
                if vertex in self.adj_list[v]:
                    self.adj_list[v].remove(vertex)

    def remove_edge(self, u, v):
        # Удаление ребра между вершинами u и v
        if u in self.adj_list and v in self.adj_list:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)  # Для неориентированного графа удаляем обратное ребро

    def get_adjacent_vertices(self, vertex):
        # Возвращает список соседних вершин для данной вершины
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            return []

    def get_all_vertices(self):
        # Возвращает список всех вершин в графе
        return list(self.adj_list.keys())

    def __str__(self):
        # Возвращает строковое представление списка смежности графа
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
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "D")
    graph.add_edge("A", "D")

    # Вывод списка смежности
    print(graph)
