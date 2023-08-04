class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # Вставка ключа в дерево
        if not node:
            return Node(key)

        # Обычная вставка в двоичное дерево поиска
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        # Обновляем высоту текущего узла
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Проверяем и восстанавливаем баланс текущего узла
        balance = self._get_balance(node)

        # Если узел несбалансирован, выполняем повороты
        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Выполняем левый поворот
        y.left = z
        z.right = T2

        # Обновляем высоты узлов
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Выполняем правый поворот
        x.right = y
        y.left = T2

        # Обновляем высоты узлов
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def print_tree(self):
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node:
            self._print_tree_recursive(node.left)
            print(node.key, end=' ')
            self._print_tree_recursive(node.right)


if __name__ == "__main__":
    avl_tree = AVLTree()
    keys_to_insert = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys_to_insert:
        avl_tree.insert(key)

    print("AVL Tree:")
    avl_tree.print_tree()
