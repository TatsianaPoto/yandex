def count_operations(n, numbers):
    # Находим минимальное и максимальное число в исходной последовательности
    min_num = min(numbers)
    max_num = max(numbers)
    operations_count = 0

    # Пока максимальное число больше, чем два раза минимальное число,
    # выполняем операцию вычитания и уменьшаем максимальное число
    while max_num > 2 * min_num:
        max_num_index = numbers.index(max_num)  # Находим индекс максимального числа
        max_num //= 2  # Делим максимальное число на 2
        numbers[max_num_index] = max_num  # Обновляем значение максимального числа в последовательности
        operations_count += 1  # Увеличиваем счетчик операций

    # Когда максимальное число станет меньше или равно двум минимальным числам,
    # выполняем операции вычитания до тех пор, пока все числа не станут одинаковыми
    while len(set(numbers)) > 1:
        max_num = max(numbers)  # Находим максимальное число
        min_num = min(numbers)  # Находим минимальное число
        diff = max_num - min_num  # Вычисляем разницу между максимальным и минимальным числом
        max_num_index = numbers.index(max_num)  # Находим индекс максимального числа
        numbers[max_num_index] = diff  # Обновляем значение максимального числа в последовательности
        operations_count += 1  # Увеличиваем счетчик операций

    return operations_count

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    result = count_operations(n, numbers)
    print(result)



"""
Алгоритм имеет сложность O(n * log(Mn)), где n - количество чисел в последовательности, 
а Mn - максимальное число в исходном наборе.

"""
