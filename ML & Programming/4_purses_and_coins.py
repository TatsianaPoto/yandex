def can_reconstruct_sum(n, wallet_amounts, total_sum):
    dp = [False] * (total_sum + 1)
    dp[0] = True

    for wallet_amount in wallet_amounts:
        for s in range(total_sum, wallet_amount - 1, -1):
            dp[s] = dp[s] or dp[s - wallet_amount]

    return dp[total_sum]

if __name__ == "__main__":
    n = int(input())
    wallet_amounts = list(map(int, input().split()))
    total_sum = int(input())

    if can_reconstruct_sum(n, wallet_amounts, total_sum):
        print("Yes")
    else:
        print("No")


"""
Давайте оценим сложность данного алгоритма.
Создание массива dp размером total_sum + 1 занимает O(total_sum) времени и памяти.
Вложенные циклы:
Внешний цикл выполняется для каждого wallet_amount в списке wallet_amounts, 
который содержит n элементов. Время выполнения внешнего цикла: O(n).
Внутренний цикл выполняется total_sum - wallet_amount раз, где wallet_amount - 
это текущий элемент из списка wallet_amounts. Время выполнения внутреннего цикла: O(total_sum).
Внутри внутреннего цикла выполняется операция dp[s] = dp[s] or dp[s - wallet_amount]. 
Операция or имеет константное время выполнения O(1).

Таким образом, общая сложность алгоритма составляет O(total_sum * n). 
Обратите внимание, что сложность может зависеть от суммы total_sum и количества элементов в списке wallet_amounts n. 
В худшем случае, когда total_sum и n сравнимы по величине, сложность алгоритма можно приближенно оценить как O(n^2).

Данный алгоритм хорошо масштабируется и быстро обрабатывает небольшие значения total_sum и n. 
Однако, при больших значениях total_sum и n алгоритм может быть замедлен.

"""