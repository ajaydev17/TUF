def print_1_to_n_backtracking(number):
    if number == 0:
        return

    print_1_to_n_backtracking(number - 1)
    print(number)


print_1_to_n_backtracking(10)
