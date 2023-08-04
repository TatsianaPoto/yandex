import random

class SkipNode:
    def __init__(self, value, level):
        # Конструктор класса SkipNode
        # value - значение узла
        # level - количество skip-уровней для данного узла
        self.value = value
        self.forward = [None] * (level + 1)  # Массив ссылок на следующие узлы на каждом уровне


class SkipList:
    def __init__(self, max_level=16, p=0.5):
        # Конструктор класса SkipList
        # max_level - максимальный уровень списка
        # p - вероятность создания skip-уровня для каждого узла
        self.max_level = max_level
        self.p = p
        self.head = self.create_node(0, max_level)  # Головной узел списка

    def create_node(self, value, level):
        # Метод для создания нового узла с заданным значением и указанным количеством skip-уровней
        return SkipNode(value, level)

    def random_level(self):
        # Метод для генерации случайного уровня с вероятностью p
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        # Метод для вставки нового узла с заданным значением в список
        update = [None] * (self.max_level + 1)  # Массив для хранения ссылок на узлы для обновления forward ссылок
        current = self.head
        for i in range(self.max_level, -1, -1):
            # Ищем место для вставки нового узла на каждом уровне, начиная с верхнего
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        level = self.random_level()  # Генерируем случайный уровень для нового узла
        new_node = self.create_node(value, level)

        for i in range(level + 1):
            # Обновляем forward ссылки на каждом уровне для нового узла и его соседних узлов
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        # Метод для поиска заданного значения в списке
        current = self.head
        for i in range(self.max_level, -1, -1):
            # Ищем заданное значение на каждом уровне, начиная с верхнего
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        
        # Переходим на следующий узел на первом уровне
        current = current.forward[0]

        if current and current.value == value:
            return current  # Найден узел с заданным значением
        else:
            return None  # Значение не найдено

    def print_list(self):
        # Метод для вывода значений всех узлов списка
        current = self.head.forward[0]
        while current:
            print(current.value, end=" -> ")
            current = current.forward[0]
        print("None")  # Выводим None в конце списка


# Пример использования списка с пропусками:
if __name__ == "__main__":
    skip_list = SkipList()
    values = [3, 6, 1, 8, 9, 2, 5, 7, 4]
    for value in values:
        skip_list.insert(value)

    skip_list.print_list()  # Выведет: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None

    result = skip_list.search(5)
    if result:
        print("Значение 5 найдено в списке.")
    else:
        print("Значение 5 не найдено в списке.")
