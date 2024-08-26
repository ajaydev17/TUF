def factorial_of_a_number(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial_of_a_number(number-1)


print(factorial_of_a_number(5))
