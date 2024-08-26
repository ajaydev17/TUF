def sum_of_n_numbers(numbers, n=None):
    if n is None:
        n = len(numbers)

    if n == 0:
        return 0

    return numbers[n - 1] + sum_of_n_numbers(numbers, n - 1)


print(sum_of_n_numbers([1, 2, 3, 4, 5]))
