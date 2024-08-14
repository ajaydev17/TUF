def find_gcd(a: int, b: int) -> int:

    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b

    return a


print(f'GCD is: {find_gcd(18, 63)}')