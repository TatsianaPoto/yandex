def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        current_element = arr[i]
        j = i - 1

        # Сравниваем текущий элемент с элементами в отсортированной части списка
        # и сдвигаем элементы вправо, пока не найдём место для текущего элемента
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем текущий элемент на найденное место
        arr[j + 1] = current_element

if __name__ == "__main__":
    # Пример использования
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    print("Отсортированный массив:", arr)
