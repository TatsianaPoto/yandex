def count_jewels_in_stones(J, S):
    jewels_count = 0
    for stone in S:
        if stone in J:
            jewels_count += 1
    return jewels_count

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        J = f.readline().strip()
        S = f.readline().strip()

    result = count_jewels_in_stones(J, S)

    with open("output.txt", "w") as f:
        f.write(str(result))