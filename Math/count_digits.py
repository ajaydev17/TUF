def count_digits(number: int):
    count = 0
    temp = number

    if temp < 0:
        temp = temp * -1

    while temp > 0:
        count = count + 1
        temp = temp // 10

    return count


print(f"Number of digits: {count_digits(1729)}")

