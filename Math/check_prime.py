def check_prime(number: int):

    count = 0

    for i in range(1, number + 1):
        if i * i >= number:
            break

        if number % i == 0:
            count = count + 1

            if number // i != i:
                count = count + 1

    if count == 2:
        return True
    else:
        return False


print(f'Is number prime: {check_prime(17)}')
