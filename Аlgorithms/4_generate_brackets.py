def generate_brackets(n, seq="", open_brackets=0, close_brackets=0):
    if len(seq) == 2 * n:
        print(seq)
        return

    if open_brackets < n:
        generate_brackets(n, seq + "(", open_brackets + 1, close_brackets)

    if close_brackets < open_brackets:
        generate_brackets(n, seq + ")", open_brackets, close_brackets + 1)

if __name__ == "__main__":
    n = int(input())
    generate_brackets(n)