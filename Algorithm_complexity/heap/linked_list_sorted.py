class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MinHeap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Создаем новый узел с заданным значением
        new_node = ListNode(value)

        # Если куча пуста, делаем новый узел корнем
        if not self.root:
            self.root = new_node
            return

        # Иначе вставляем новый узел в отсортированный связный список
        if value < self.root.val:
            new_node.next = self.root
            self.root = new_node
            return

        current = self.root
        while current.next and value >= current.next.val:
            current = current.next

        # Вставляем новый узел после текущего узла
        new_node.next = current.next
        current.next = new_node

    def extract_min(self):
        # Извлекаем минимальное значение из корня и обновляем корень
        if self.root:
            min_val = self.root.val
            self.root = self.root.next
            return min_val

    def is_empty(self):
        return not bool(self.root)


# Пример использования:
if __name__ == "__main__":
    min_heap = MinHeap()

    # Вставка элементов в кучу
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(10)
    min_heap.insert(2)
    min_heap.insert(7)

    # Извлечение минимального значения
    while not min_heap.is_empty():
        print(min_heap.extract_min(), end=' ')  # Выведет: 2 3 5 7 10
