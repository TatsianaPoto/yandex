class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.marked = False


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

    def insert(self, key):
        # Создаем новый узел и добавляем его в список корней
        new_node = FibonacciHeapNode(key)
        if not self.min_node:
            self.min_node = new_node
        else:
            self._link(self.min_node, new_node)
            if new_node.key < self.min_node.key:
                self.min_node = new_node

        self.num_nodes += 1

    def find_min(self):
        return self.min_node.key if self.min_node else None

    def extract_min(self):
        if not self.min_node:
            return None

        min_node = self.min_node
        if min_node.child:
            # Перемещаем детей минимального узла в список корней
            child = min_node.child
            while child.parent:
                child.parent = None
                child = child.right

            self.min_node = self._merge_lists(self.min_node, min_node.child)
        else:
            self.min_node = min_node.right

        if min_node == min_node.right:
            self.min_node = None
        else:
            self._consolidate()

        self.num_nodes -= 1

        return min_node.key

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key")

        node.key = new_key
        parent = node.parent

        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min_node.key:
            self.min_node = node

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    def _link(self, node1, node2):
        # Узел node2 становится ребенком узла node1
        node2.parent = node1
        if not node1.child:
            node1.child = node2
        else:
            node2.right = node1.child.right
            node2.left = node1.child
            node1.child.right.left = node2
            node1.child.right = node2

        node1.degree += 1

    def _merge_lists(self, node1, node2):
        # Слияние двух списков корней
        if not node1:
            return node2
        if not node2:
            return node1

        node1.right.left = node2
        node2.right.left = node1
        node1.right, node2.right = node2.right, node1.right

        return node1 if node1.key < node2.key else node2

    def _consolidate(self):
        max_degree = (self.num_nodes.bit_length() - 1) + 1
        degree_table = [None] * max_degree

        nodes = [self.min_node]
        current_node = self.min_node.right
        while current_node != self.min_node:
            nodes.append(current_node)
            current_node = current_node.right

        for node in nodes:
            degree = node.degree
            while degree_table[degree]:
                other_node = degree_table[degree]
                if node.key > other_node.key:
                    node, other_node = other_node, node
                self._link(node, other_node)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node

        self.min_node = None
        for node in degree_table:
            if node:
                if not self.min_node:
                    self.min_node = node
                elif node.key < self.min_node.key:
                    self.min_node = node

    def _cut(self, node, parent):
        # Удаление ребра между node и его родителем
        if node.right == node:
            parent.child = None
        else:
            parent.child = node.right
            node.right.left = node.left
            node.left.right = node.right

        parent.degree -= 1
        node.parent = None
        node.marked = False
        self.min_node = self._merge_lists(self.min_node, node)

    def _cascading_cut(self, node):
        parent = node.parent
        if parent:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def is_empty(self):
        return not bool(self.min_node)


# Пример использования:
if __name__ == "__main__":
    fibonacci_heap = FibonacciHeap()

    # Вставка элементов в кучу
    fibonacci_heap.insert(5)
    fibonacci_heap.insert(3)
    fibonacci_heap.insert(10)
    fibonacci_heap.insert(2)
    fibonacci_heap.insert(7)

    # Извлечение минимального значения
    while not fibonacci_heap.is_empty():
        print(fibonacci_heap.extract_min(), end=' ')  # Выведет: 2 3 5 7 10
