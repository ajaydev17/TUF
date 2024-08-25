def print_n_to_1_backtracking(number, start=1):
    if start > number:
        return

    print_n_to_1_backtracking(number, start + 1)
    print(start)


print_n_to_1_backtracking(10)
