def print_all_divisors(number: int):

    print(f'All divisors of {number} are...')

    for i in range(1, number + 1):
        if i * i >= number:
            break

        if number % i == 0:
            print(i)

            if number // i != i:
                print(number // i)


print_all_divisors(1729)
