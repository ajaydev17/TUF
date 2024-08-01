# *********
#  *******
#   *****
#    ***
#     *

# prints the above pattern

def print_triangle(n: int) -> None:
    for i in range(0, n):

        # print space
        for _ in range(0, i):
            print(' ', end='')

        # print *
        for _ in range(0, 2 * n - 2 * i - 1):
            print('*', end='')

        # print space
        for _ in range(0, i):
            print(' ', end='')

        print()


print_triangle(5)
