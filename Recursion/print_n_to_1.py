def print_n_to_1(start, number):
    if start == 0:
        return

    print(start)
    print_n_to_1(start - 1, number)


print_n_to_1(10, 10)

