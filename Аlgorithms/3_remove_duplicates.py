def remove_duplicates(input_file, output_file):
    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        n = int(f_in.readline().strip())
        prev_num = None

        for _ in range(n):
            num = int(f_in.readline().strip())
            if num != prev_num:
                f_out.write(str(num) + "\n")
                prev_num = num

if __name__ == "__main__":
    remove_duplicates("input.txt", "output.txt")