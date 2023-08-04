def apply_permutation(perm, positions):
    """
    Применяет перестановку perm к позициям positions и возвращает новые позиции.
    """
    new_positions = [positions[perm[i] - 1] for i in range(len(perm))]
    return new_positions

def find_first_position(n, m, permutations, initial_permutations):
    """
    Находит позицию первого элемента, если последовательно применить все перестановки,
    кроме одной из списка initial_permutations.
    """
    positions = list(range(1, n + 1))

    # Вычисляем prefix[i] для i от 1 до k
    prefix = [list(range(1, n + 1))]
    for perm_type in initial_permutations[:-1]:
        perm = permutations[perm_type - 1]
        prefix.append(apply_permutation(perm, prefix[-1]))

    # Вычисляем suffix[i] для i от k до 1
    suffix = [list(range(1, n + 1))]
    for perm_type in initial_permutations[:0:-1]:
        perm = permutations[perm_type - 1]
        suffix.append(apply_permutation(perm, suffix[-1]))

    # Находим позицию первого элемента после удаления j-й перестановки
    first_positions = []
    for j in range(len(initial_permutations)):
        result = apply_permutation(suffix[j+1], prefix[j-1])
        first_positions.append(min(result))

    return first_positions

if __name__ == "__main__":
    n, m = map(int, input().split())
    permutations = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    initial_permutations = list(map(int, input().split()))

    result = find_first_position(n, m, permutations, initial_permutations)
    for pos in result:
        print(pos)


"""
итоговая сложность алгоритма — O(n⋅k).
"""