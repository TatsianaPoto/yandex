# Класс для представления узла красно-черного дерева
class Node:
    def __init__(self, key, color, parent, left, right):
        self.key = key  # Ключ узла
        self.color = color  # Цвет узла (True - красный, False - черный)
        self.parent = parent  # Родительский узел
        self.left = left  # Левый дочерний узел
        self.right = right  # Правый дочерний узел


class RedBlackTree:
    def __init__(self):
        self.nil = Node(key=None, color=False, parent=None, left=None, right=None)
        self.root = self.nil

    def insert(self, key):
        # Вставка нового ключа в дерево
        new_node = Node(key=key, color=True, parent=self.nil, left=self.nil, right=self.nil)
        if not self.root:
            # Если дерево пустое, новый узел становится корнем
            self.root = new_node
        else:
            # Вставка узла в дерево
            current = self.root
            while current != self.nil:
                parent = current
                if key < current.key:
                    current = current.left
                else:
                    current = current.right

            new_node.parent = parent
            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node

            self.insert_fixup(new_node)

    def insert_fixup(self, node):
        # Балансировка дерева после вставки нового узла
        while node.parent.color:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self.left_rotate(node.parent.parent)

        self.root.color = False

    def left_rotate(self, x):
        # Левый поворот дерева вокруг узла x
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        # Правый поворот дерева вокруг узла y
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def search(self, key):
        # Поиск ключа в дереве
        current = self.root
        while current != self.nil and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def print_tree(self):
        # Вывод дерева на экран (обход в порядке "инфикс")
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node != self.nil:
            self._print_tree_recursive(node.left)
            color = "Red" if node.color else "Black"
            print(f"Key: {node.key}, Color: {color}")
            self._print_tree_recursive(node.right)


if __name__ == "__main__":
    btree = RedBlackTree()

    keys_to_insert = [10, 5, 20, 7, 3, 15, 25, 1, 9]
    for key in keys_to_insert:
        btree.insert(key)

    print("Red-Black Tree:")
    btree.print_tree()

    key_to_search = 5
    result = btree.search(key_to_search)
    if result:
        print(f"Key {key_to_search} found.")
    else:
        print(f"Key {key_to_search} not found.")
