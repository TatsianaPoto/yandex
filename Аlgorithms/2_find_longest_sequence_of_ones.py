def find_longest_sequence_of_ones(n, arr):
    max_length = 0
    current_length = 0

    for i in range(n):
        if arr[i] == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0

    max_length = max(max_length, current_length)
    return max_length

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())
        arr = [int(f.readline().strip()) for _ in range(n)]

    result = find_longest_sequence_of_ones(n, arr)

    with open("output.txt", "w") as f:
        f.write(str(result))
