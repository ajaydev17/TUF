#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

# prints the above pattern

def print_triangle(n: int) -> None:
    space = 2 * (n - 1)

    for i in range(1, n + 1):

        # print space
        for j in range(1, i + 1):
            print(j, end='')

        # print *
        for _ in range(0, space):
            print(' ', end='')

        # print space
        for k in range(i, 0, -1):
            print(k, end='')

        space = space - 2

        print()


print_triangle(5)
