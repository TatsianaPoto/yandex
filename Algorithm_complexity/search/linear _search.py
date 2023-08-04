def linear_search(arr, target):
    """
    Функция линейного поиска.

    Parameters:
        arr (list): Список элементов.
        target: Искомый элемент.

    Returns:
        int: Индекс искомого элемента в списке или -1, если элемент не найден.
    """
    # Проходимся по всем элементам списка
    for index, element in enumerate(arr):
        # Сравниваем элемент с искомым элементом
        if element == target:
            # Если элемент найден, возвращаем его индекс
            return index

    # Если элемент не найден, возвращаем -1
    return -1

if __name__ == "__main__":
    # Пример списка
    arr = [5, 8, 2, 7, 10, 4, 6]

    # Искомый элемент
    target = 10

    # Вызов функции линейного поиска
    result = linear_search(arr, target)

    if result != -1:
        print(f"Искомый элемент {target} найден в списке на позиции {result}.")
    else:
        print(f"Искомый элемент {target} не найден в списке.")
