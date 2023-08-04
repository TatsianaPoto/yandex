class HashTable:
    def __init__(self, size):
        # Конструктор класса HashTable
        # size - размер хеш-таблицы (количество ячеек массива)
        self.size = size
        self.table = [[] for _ in range(size)]  # Создаем список списков (метод цепочек) для хранения пар ключ-значение

    def _hash_function(self, key):
        # Простая хеш-функция, которая возвращает остаток от деления ключа на размер хеш-таблицы
        return hash(key) % self.size

    def insert(self, key, value):
        # Метод для вставки новой пары ключ-значение в хеш-таблицу
        index = self._hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        # Метод для поиска значения по заданному ключу
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        # Метод для удаления пары ключ-значение из хеш-таблицы
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False


# Пример использования хеш-таблицы:
if __name__ == "__main__":
    hash_table = HashTable(size=10)
    hash_table.insert("apple", 10)
    hash_table.insert("banana", 20)
    hash_table.insert("orange", 30)

    print(hash_table.search("apple"))  # Выведет: 10
    print(hash_table.search("grape"))  # Выведет: None

    hash_table.remove("banana")
    print(hash_table.search("banana"))  # Выведет: None
