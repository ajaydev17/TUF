def check_palindrome(number: int):

    reverse_number = 0
    temp = number

    if temp < 0:
        temp = temp * -1

    while temp > 0:
        last_digit = temp % 10
        reverse_number = reverse_number * 10 + last_digit
        temp = temp // 10

    if number < 0:
        reverse_number = reverse_number * -1

    if number == reverse_number:
        return True

    return False


print(f"Is Palindrome: {check_palindrome(-131)}")
