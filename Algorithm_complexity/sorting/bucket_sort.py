def insertion_sort(arr):
    # Вспомогательная функция для сортировки одного блока (вставочная сортировка)
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr, bucket_size=10):
    # Блочная сортировка с использованием вставочной сортировки внутри каждой корзины
    if len(arr) == 0:
        return arr

    # Находим минимальное и максимальное значение в списке
    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1

    # Создаем пустые корзины
    buckets = [[] for _ in range(bucket_count)]

    # Распределение элементов по корзинам
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    # Сортировка каждой корзины (в данном случае используется вставочная сортировка)
    for i in range(bucket_count):
        insertion_sort(buckets[i])

    # Объединение отсортированных корзин в итоговый отсортированный список
    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

if __name__ == "__main__":
    # Пример использования
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bucket_sort(arr)
    print("Отсортированный массив:", sorted_arr)
