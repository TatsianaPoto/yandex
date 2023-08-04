class BinomialHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None


class BinomialHeap:
    def __init__(self):
        self.head = None

    def insert(self, key):
        # Создаем новый одноузловый биномиальный кучу и объединяем с текущей кучей
        new_heap = BinomialHeap()
        new_heap.head = BinomialHeapNode(key)

        self.head = self.union(self, new_heap)

    def find_min(self):
        # Находим минимальное значение, просматривая все корни биномиальных деревьев
        if not self.head:
            return None

        min_val = self.head.key
        current_node = self.head.sibling
        while current_node:
            min_val = min(min_val, current_node.key)
            current_node = current_node.sibling

        return min_val

    def extract_min(self):
        # Извлекаем минимальное значение, находим дерево с минимальным значением, и объединяем детей этого дерева с текущей кучей
        if not self.head:
            return None

        min_node = self.head
        prev_node = None
        current_node = min_node.sibling
        while current_node:
            if current_node.key < min_node.key:
                min_node = current_node
                prev_node = None
            else:
                prev_node = current_node
            current_node = current_node.sibling

        if prev_node:
            prev_node.sibling = min_node.sibling
        elif min_node == self.head:
            self.head = min_node.sibling

        # Создаем новую кучу из детей удаленного минимального дерева и объединяем ее с текущей кучей
        child_heap = BinomialHeap()
        child_heap.head = min_node.child

        self.head = self.union(self, child_heap)

        return min_node.key

    def union(self, heap1, heap2):
        # Объединение двух биномиальных куч путем слияния их деревьев
        merged_heap = BinomialHeap()
        current_node1 = heap1.head
        current_node2 = heap2.head
        current_node = None

        while current_node1 and current_node2:
            if current_node1.degree <= current_node2.degree:
                next_node = current_node1
                current_node1 = current_node1.sibling
            else:
                next_node = current_node2
                current_node2 = current_node2.sibling

            if not current_node:
                merged_heap.head = next_node
            else:
                current_node.sibling = next_node

            current_node = next_node

        if current_node1:
            current_node.sibling = current_node1
        elif current_node2:
            current_node.sibling = current_node2

        # Склеиваем деревья с одинаковой степенью
        prev_node = None
        current_node = merged_heap.head
        next_node = current_node.sibling
        while next_node:
            if current_node.degree != next_node.degree or (next_node.sibling and next_node.sibling.degree == current_node.degree):
                prev_node = current_node
                current_node = next_node
            elif current_node.key <= next_node.key:
                current_node.sibling = next_node.sibling
                next_node.parent = current_node
                next_node.sibling = current_node.child
                current_node.child = next_node
                current_node.degree += 1
            else:
                if not prev_node:
                    merged_heap.head = next_node
                else:
                    prev_node.sibling = next_node

                current_node.parent = next_node
                current_node.sibling = next_node.child
                next_node.child = current_node
                next_node.degree += 1

                current_node = next_node

            next_node = current_node.sibling

        return merged_heap

    def is_empty(self):
        return not bool(self.head)


# Пример использования:
if __name__ == "__main__":
    binomial_heap = BinomialHeap()

    # Вставка элементов в кучу
    binomial_heap.insert(5)
    binomial_heap.insert(3)
    binomial_heap.insert(10)
    binomial_heap.insert(2)
    binomial_heap.insert(7)

    # Извлечение минимального значения
    while not binomial_heap.is_empty():
        print(binomial_heap.extract_min(), end=' ')  # Выведет: 2 3 5 7 10
