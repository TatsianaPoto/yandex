class MyArray:
    def __init__(self, size):
        # Инициализация массива заданного размера
        self.size = size
        self.data = [None] * size

    def set(self, index, value):
        # Установка значения элемента по индексу
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Индекс выходит за пределы массива")

    def get(self, index):
        # Получение значения элемента по индексу
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Индекс выходит за пределы массива")

if __name__ == "__main__":
    # Пример использования
    my_array = MyArray(5)
    my_array.set(0, 10)
    my_array.set(1, 20)
    my_array.set(2, 30)

    print(my_array.get(0))  # Выведет 10
    print(my_array.get(1))  # Выведет 20
    print(my_array.get(2))  # Выведет 30
