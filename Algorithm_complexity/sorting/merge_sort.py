def merge_sort(arr):
    # Базовый случай: если массив пустой или содержит только один элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Объединяем отсортированные половины в один отсортированный массив
    merged_arr = merge(left_half, right_half)
    return merged_arr

def merge(left, right):
    merged_arr = []
    left_idx, right_idx = 0, 0

    # Слияние двух отсортированных массивов
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged_arr.append(left[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right[right_idx])
            right_idx += 1

    # Добавляем оставшиеся элементы из левого и правого массивов
    merged_arr.extend(left[left_idx:])
    merged_arr.extend(right[right_idx:])
    return merged_arr

if __name__ == "__main__":
    # Пример использования
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
