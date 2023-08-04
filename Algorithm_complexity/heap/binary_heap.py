class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Вставка нового значения в конец кучи
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)  # Поддержка свойств кучи

    def extract_min(self):
        if not self.heap:
            return None

        # Извлечение минимального значения
        min_val = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            # Перемещаем последний элемент на вершину и восстанавливаем свойства кучи
            self.heap[0] = last_val
            self._sift_down(0)

        return min_val

    def _sift_up(self, index):
        # Восстановление свойств кучи при вставке нового значения
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _sift_down(self, index):
        # Восстановление свойств кучи при извлечении минимального значения
        while 2 * index + 1 < len(self.heap):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            min_child_index = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[left_child_index]:
                min_child_index = right_child_index

            if self.heap[index] > self.heap[min_child_index]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

    def is_empty(self):
        return not bool(self.heap)


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
