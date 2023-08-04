def counting_sort(arr, exp):
    # Стабильная сортировка подсчетом по заданному разряду (цифре)
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Заполнение массива count для подсчета количества элементов по каждой цифре
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Обновление массива count для получения актуальных позиций элементов
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Построение выходного списка, сохраняя стабильность сортировки
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Копирование отсортированного списка обратно в исходный
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Определение максимального значения для определения количества разрядов
    max_val = max(arr)

    # Применение сортировки подсчетом для каждого разряда, начиная с младшего
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

if __name__ == "__main__":
    # Пример использования
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)
    print("Отсортированный массив:", arr)
