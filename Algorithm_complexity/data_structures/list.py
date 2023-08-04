# Создание пустого списка
my_list = []

# Добавление элементов в список
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Доступ по индексу
print(my_list[0])  # Выведет 10
print(my_list[1])  # Выведет 20
print(my_list[2])  # Выведет 30

# Удаление элемента по значению
my_list.remove(20)

# Динамический массив автоматически изменяет свой размер
my_list.append(40)
my_list.append(50)

print(my_list)  # Выведет [10, 30, 40, 50]
