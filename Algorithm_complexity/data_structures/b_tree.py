# Класс для представления узла B-дерева
class BTreeNode:
    def __init__(self, leaf=True):
        # Конструктор класса BTreeNode
        self.leaf = leaf  # Флаг, указывающий, является ли узел листом
        self.keys = []  # Список ключей в узле
        self.children = []  # Список потомков узла


class BTree:
    def __init__(self, order):
        # Конструктор класса BTree
        self.root = BTreeNode(leaf=True)  # Корень дерева
        self.order = order  # Максимальное количество ключей в узле (M)

    def insert(self, key):
        # Метод для вставки нового ключа в B-дерево
        root = self.root

        if len(root.keys) == self.order - 1:
            # Если корень заполнен, создаем новый корень
            new_root = BTreeNode(leaf=False)
            self.root = new_root
            new_root.children.append(root)
            self.split_child(new_root, 0)

        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        # Рекурсивный метод для вставки ключа в не заполненный узел
        i = len(node.keys) - 1

        if node.leaf:
            # Если узел является листом, вставляем ключ в правильную позицию
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            # Если узел не является листом, находим подходящий потомок и рекурсивно вызываем insert_non_full для него
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == self.order - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        # Метод для разделения полностью заполненного узла
        child = parent.children[index]
        new_node = BTreeNode(leaf=child.leaf)
        parent.keys.insert(index, child.keys[self.order // 2])
        parent.children.insert(index + 1, new_node)
        new_node.keys = child.keys[self.order // 2 + 1:]
        child.keys = child.keys[:self.order // 2]

        if not child.leaf:
            new_node.children = child.children[self.order // 2 + 1:]
            child.children = child.children[:self.order // 2 + 1]

    def search(self, key):
        # Метод для поиска ключа в B-дереве
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        # Рекурсивный метод для поиска ключа в узле
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node
        elif node.leaf:
            return None
        else:
            return self._search_recursive(node.children[i], key)

    def print_tree(self):
        # Метод для печати B-дерева
        self._print_recursive(self.root)

    def _print_recursive(self, node, level=0):
        # Рекурсивный метод для печати узла
        if node is not None:
            print(f"Level {level}, Keys: {node.keys}")
            if not node.leaf:
                for child in node.children:
                    self._print_recursive(child, level + 1)


# Пример использования B-дерева:
if __name__ == "__main__":
    btree = BTree(order=3)
    for key in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        btree.insert(key)

    print("B-tree after insertion:")
    btree.print_tree()

    key_to_search = 5
    result = btree.search(key_to_search)
    if result:
        print(f"Key {key_to_search} found.")
    else:
        print(f"Key {key_to_search} not found.")
