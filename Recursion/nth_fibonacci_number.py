def nth_fibonacci_number(number):
    if number == 0:
        return 0

    if number == 1:
        return 1

    return nth_fibonacci_number(number - 1) + nth_fibonacci_number(number - 2)


print(nth_fibonacci_number(100))
