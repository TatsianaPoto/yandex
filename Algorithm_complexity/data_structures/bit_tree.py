class TreeNode:
    def __init__(self, value):
        # Конструктор класса TreeNode
        # value - значение узла
        self.value = value
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок


class BinarySearchTree:
    def __init__(self):
        # Конструктор класса BinarySearchTree
        self.root = None  # Корень дерева

    def insert(self, value):
        # Метод для вставки нового значения в дерево
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        # Рекурсивный метод для вставки нового значения в дерево
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def search(self, value):
        # Метод для поиска значения в дереве
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        # Рекурсивный метод для поиска значения в дереве
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursively(node.left, value)
        return self._search_recursively(node.right, value)

    def delete(self, value):
        # Метод для удаления значения из дерева
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
        # Рекурсивный метод для удаления значения из дерева
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_min(node.right)
            node.value = temp.value
            node.right = self._delete_recursively(node.right, temp.value)
        return node

    def _find_min(self, node):
        # Метод для поиска минимального значения в поддереве
        while node.left:
            node = node.left
        return node


# Пример использования бинарного дерева поиска:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print(bst.search(30).value)  # Выведет: 30

    bst.delete(30)
    print(bst.search(30))  # Выведет: None
