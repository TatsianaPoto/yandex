def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Находим индекс минимального элемента в неотсортированной части списка
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Меняем местами минимальный элемент с первым элементом неотсортированной части
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    # Пример использования
    arr = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(arr)
    print("Отсортированный массив:", arr)
