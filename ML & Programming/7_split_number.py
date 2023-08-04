def split_number(n):
    if n == 0:
        return "0"

    split = []
    digits = []
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10

    prev_digit = None
    for digit in reversed(digits):
        if digit != 0:
            if prev_digit is not None and prev_digit != 0:
                split.append("-")
            split.append(str(digit))
        prev_digit = digit

    return "-".join(split)

if __name__ == "__main__":
    n = int(input())
    result = split_number(n)
    print(result)


"""
Давайте оценим сложность данного алгоритма.
Заполнение списка digits занимает O(log n) времени, где n - входное число, 
так как мы разбиваем число на отдельные цифры.
Построение списка split занимает O(log n) времени, так как мы обрабатываем каждую цифру 
в списке digits и добавляем или пропускаем её.
Объединение элементов списка split с помощью "-" занимает O(log n) времени.

Общая сложность алгоритма можно оценить как O(log n). 
Это хорошая сложность, так как алгоритм работает эффективно и быстро обрабатывает числа с большим количеством цифр.
"""