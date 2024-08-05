# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


# prints the above pattern

def print_triangle(n: int) -> None:
    for i in range(1, 2 * n + 1):

        number_of_stars = i

        if i > n:
            number_of_stars = 2 * n - i

        for _ in range(1, number_of_stars + 1):
            print('*', end='')

        print()


print_triangle(5)
