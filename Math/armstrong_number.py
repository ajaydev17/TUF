def armstrong_number(number: int):

    sum = 0
    temp = number

    while temp > 0:
        last_digit = temp % 10
        sum = sum + last_digit ** 3
        temp = temp // 10

    if number == sum:
        return True
    else:
        return False


print(f"Is Armstrong Number: {armstrong_number(153)}")
