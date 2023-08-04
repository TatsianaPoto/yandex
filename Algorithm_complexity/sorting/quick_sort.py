def quick_sort(arr):
    # Базовый случай: если массив пустой или содержит только один элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент
    pivot = arr[len(arr) // 2]

    # Разделяем элементы на две подгруппы: меньше опорного и больше опорного
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортируем подгруппы
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Пример использования
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)
