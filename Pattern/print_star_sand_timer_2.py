# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# prints the above pattern

def print_triangle(n: int) -> None:
    space = 2 * (n - 1)

    for i in range(1, 2 * n):

        star = i
        if i > n:
            star = 2 * n - i

        # print *
        for j in range(1, star + 1):
            print('*', end='')

        # print space
        for _ in range(1, space + 1):
            print(' ', end='')

        # print space
        for k in range(1, star + 1):
            print('*', end='')

        if i < n:
            space = space - 2
        else:
            space = space + 2

        print()


print_triangle(5)