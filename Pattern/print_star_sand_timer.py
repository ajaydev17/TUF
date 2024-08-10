# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


# prints the above pattern

def print_triangle(n: int) -> None:
    space = 0

    for i in range(0, n):

        # print *
        for j in range(0, n - i):
            print('*', end='')

        # print space
        for _ in range(0, space):
            print(' ', end='')

        # print space
        for k in range(0, n - i):
            print('*', end='')

        space = space + 2

        print()

    space = 2 * (n - 1)

    for i in range(1, n + 1):

        # print *
        for j in range(1, i + 1):
            print('*', end='')

        # print space
        for _ in range(0, space):
            print(' ', end='')

        # print *
        for k in range(i, 0, -1):
            print('*', end='')

        space = space - 2

        print()


print_triangle(5)