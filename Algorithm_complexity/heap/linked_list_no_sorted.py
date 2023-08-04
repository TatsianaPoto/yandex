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

        # Иначе вставляем новый узел в начало связного списка
        new_node.next = self.root
        self.root = new_node

    def extract_min(self):
        # Ищем узел с минимальным значением
        min_node = self.root
        prev_node = None
        current = self.root

        while current:
            if current.val < min_node.val:
                min_node = current
                if prev_node:
                    prev_node.next = current.next
                else:
                    self.root = current.next
            prev_node = current
            current = current.next

        # Извлекаем минимальное значение и обновляем корень
        if min_node:
            min_val = min_node.val
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
