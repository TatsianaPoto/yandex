def count_red_black_trees(n):
    MOD = 10**9 + 7

    # Количество неизоморфных красных и черных деревьев с i вершинами и h черными вершинами от корня
    count_black = [[0 for _ in range(n+1)] for _ in range(n+1)]
    count_red = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Инициализация базовых случаев
    for i in range(n+1):
        count_black[i][0] = 1

    for i in range(1, n+1):
        for h in range(1, n+1):
            for j in range(i):
                # Вычисление количества черных и красных деревьев с i вершинами и h черными вершинами от корня
                if j < i - 1:
                    count_black[i][h] = (count_black[i][h] + count_black[j][h-1] * count_black[i-j-1][h-1]) % MOD
                else:
                    count_black[i][h] = (count_black[i][h] + count_black[j][h-1] * (count_black[i-j-1][h-1] + count_red[i-j-1][h-1])) % MOD
                count_red[i][h] = (count_red[i][h] + count_black[j][h] * count_black[i-j-1][h-1]) % MOD

    return count_black[n][n]

if __name__ == "__main__":
    n = int(input())
    ans = count_red_black_trees(n)
    print(ans)


# TODO Сложная задачка, требует времени и визуализации, пока мне не по зубам)

"""
"""