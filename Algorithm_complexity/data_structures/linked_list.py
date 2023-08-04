class Node:
    def __init__(self, value):
        # Конструктор класса Node
        # value - значение узла
        self.value = value
        self.next = None  # Ссылка на следующий узел, изначально устанавливаем в None


class SinglyLinkedList:
    def __init__(self):
        # Конструктор класса SinglyLinkedList
        self.head = None  # Указатель на первый узел, изначально устанавливаем в None

    def append(self, value):
        # Метод для добавления нового узла с указанным значением в конец списка
        # value - значение нового узла
        new_node = Node(value)  # Создаем новый узел с заданным значением

        if self.head is None:
            # Если список пустой, то новый узел становится первым (головой) списка
            self.head = new_node
        else:
            # Иначе находим последний узел и добавляем новый узел после него
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        # Метод для вывода значений всех узлов списка
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # Выводим None в конце списка

    def search(self, value):
        # Метод для поиска узла с заданным значением в списке
        # value - значение, которое нужно найти
        current = self.head
        while current is not None:
            if current.value == value:
                return True  # Узел с заданным значением найден
            current = current.next
        return False  # Узел с заданным значением не найден


# Пример использования односвязного списка:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    linked_list.print_list()  # Выведет: 10 -> 20 -> 30 -> None

    print(linked_list.search(20))  # Выведет: True, так как значение 20 присутствует в списке
    print(linked_list.search(40))  # Выведет: False, так как значение 40 отсутствует в списке
