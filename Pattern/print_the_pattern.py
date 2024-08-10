# *****
# *   *
# *   *
# *   *
# *****


# prints the above pattern

def print_triangle(n: int) -> None:

    for i in range(0, 2 * n - 1):

        # print *
        for j in range(0, 2 * n - 1):

            top = i
            left = j
            right = 2 * n - 2 - j
            bottom = 2 * n - 2 - i

            value = n - min(min(top, bottom), min(right, left))
            print(value, end='')

        print()


print_triangle(4)
