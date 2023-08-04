class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
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

        # Проводим splay операцию, чтобы переместить вставленный узел в корень
        return self._splay(node, key)

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root

    def _splay(self, node, key):
        if not node or node.key == key:
            return node

        if key < node.key:
            # Ключ в левом поддереве, выполняем левый поворот
            if not node.left:
                return node
            if key < node.left.key:
                # Zig-Zig
                node.left.left = self._splay(node.left.left, key)
                node = self._rotate_right(node)
            elif key > node.left.key:
                # Zig-Zag
                node.left.right = self._splay(node.left.right, key)
                if node.left.right:
                    node.left = self._rotate_left(node.left)
            if node.left:
                return self._rotate_right(node)
            else:
                return node
        else:
            # Ключ в правом поддереве, выполняем правый поворот
            if not node.right:
                return node
            if key < node.right.key:
                # Zag-Zig
                node.right.left = self._splay(node.right.left, key)
                if node.right.left:
                    node.right = self._rotate_right(node.right)
            elif key > node.right.key:
                # Zag-Zag
                node.right.right = self._splay(node.right.right, key)
                node = self._rotate_left(node)
            if node.right:
                return self._rotate_left(node)
            else:
                return node

    def _rotate_left(self, node):
        # Левый поворот дерева вокруг узла
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def _rotate_right(self, node):
        # Правый поворот дерева вокруг узла
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def print_tree(self):
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node:
            self._print_tree_recursive(node.left)
            print(node.key, end=' ')
            self._print_tree_recursive(node.right)


if __name__ == "__main__":
    splay_tree = SplayTree()
    keys_to_insert = [10, 5, 20, 7, 3, 15, 25, 1, 9]
    for key in keys_to_insert:
        splay_tree.insert(key)

    print("Splay Tree:")
    splay_tree.print_tree()

    key_to_search = 5
    result = splay_tree.search(key_to_search)
    if result:
        print(f"\nKey {key_to_search} found.")
        print("Splay Tree after search:")
        splay_tree.print_tree()
    else:
        print(f"Key {key_to_search} not found.")
