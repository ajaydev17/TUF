def print_1_to_n(number, start=1):
    if start > number:
        return

    print(start)
    print_1_to_n(number, start + 1)


print_1_to_n(10)
