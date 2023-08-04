def heapify(arr, n, i):
    largest = i  # Изначально предполагаем, что наибольший элемент - это корень (i)
    left = 2 * i + 1
    right = 2 * i + 2

    # Если левый дочерний элемент существует и больше корня
    if left < n and arr[i] < arr[left]:
        largest = left

    # Если правый дочерний элемент существует и больше корня
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если сам корень не является наибольшим, меняем местами с наибольшим дочерним элементом
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Рекурсивно просеиваем вниз измененную подкучу
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение кучи (перегруппируем массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы из кучи по одному и уменьшаем размер кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

if __name__ == "__main__":
    # Пример использования
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    heap_sort(arr)
    print(arr)
