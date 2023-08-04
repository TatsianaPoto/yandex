import random
import time

def calculate_digit_sum(num):
    return sum(int(digit) for digit in str(num))

def is_complex(num):
    for k in range(1, num + 1):
        k_squared = k * k
        if 3 * k == num * calculate_digit_sum(k_squared):
            return True
    return False

def find_smallest_complex_number(upper_bound):
    complex_numbers = set()

    for n in range(1, upper_bound + 1):
        if is_complex(n):
            complex_numbers.add(n)

    smallest = 1
    while True:
        if smallest not in complex_numbers:
            return smallest
        smallest += 1

if __name__ == "__main__":
    upper_bound = 1000  # Максимальное значение для перебора (можно увеличить для большей надежности)
    smallest_complex_number = find_smallest_complex_number(upper_bound)
    print("Наименьшее сложное число:", smallest_complex_number)

    # Установим начальную точку генератора случайных чисел в текущее время в миллисекундах
    random.seed(int(time.time() * 1000))

    random_number = random.randint(1, smallest_complex_number)
    print("Случайно сгенерированное число:", random_number)



"""
Давайте оценим сложность данного алгоритма.
Функция calculate_digit_sum(num) проходит по всем цифрам числа num, чтобы вычислить их сумму. 
Если num содержит k цифр, то сложность этой функции будет O(k).
Функция is_complex(num) вызывается для каждого числа от 1 до num. 
Внутри этой функции выполняется простая арифметическая операция и вызывается функция calculate_digit_sum, 
что занимает O(k). В итоге, сложность этой функции для каждого числа num составит O(k).
Функция find_smallest_complex_number(upper_bound) вызывает функцию is_complex 
для каждого числа от 1 до upper_bound. Следовательно, сложность этой функции составит O(upper_bound * k), 
где k - максимальное количество цифр в числе upper_bound.
В основной части программы вызывается функция find_smallest_complex_number с аргументом upper_bound. 
Затем выполняется цикл while, который в худшем случае выполняется smallest_complex_number раз, 
где smallest_complex_number - значение, возвращенное функцией find_smallest_complex_number. 
Внутри цикла выполняются простые операции, такие как проверка принадлежности числа множеству, что занимает O(1).

Таким образом, общая сложность алгоритма составляет O(upper_bound * k + smallest_complex_number), 
где k - максимальное количество цифр в числе upper_bound.
 В худшем случае, когда upper_bound и smallest_complex_number сравнимы по величине, 
 сложность алгоритма можно приближенно оценить как O(n * k), 
 где n - максимальное значение из upper_bound и smallest_complex_number.
"""