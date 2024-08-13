def count_digits(number: int):

    count = 0

    while number > 0:
        count = count + 1
        number = number // 10

    return count


print(f"Number of digits: {count_digits(1729)}")
