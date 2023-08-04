class Node:
    def __init__(self, value):
        # Конструктор класса Node
        # value - значение узла
        self.value = value
        self.prev = None  # Ссылка на предыдущий узел, изначально устанавливаем в None
        self.next = None  # Ссылка на следующий узел, изначально устанавливаем в None


class DoublyLinkedList:
    def __init__(self):
        # Конструктор класса DoublyLinkedList
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
            new_node.prev = current  # Устанавливаем ссылку на предыдущий узел для нового узла

    def print_forward(self):
        # Метод для вывода значений всех узлов списка в прямом порядке
        current = self.head
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")  # Выводим None в конце списка

    def print_backward(self):
        # Метод для вывода значений всех узлов списка в обратном порядке
        current = self.head
        while current.next is not None:
            current = current.next
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")  # Выводим None в конце списка


# Пример использования двусвязного списка:
if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    linked_list.print_forward()  # Выведет: 10 <-> 20 <-> 30 <-> None
    linked_list.print_backward()  # Выведет: 30 <-> 20 <-> 10 <-> None
