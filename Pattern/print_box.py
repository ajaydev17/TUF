# *****
# *   *
# *   *
# *   *
# *****


# prints the above pattern

def print_triangle(n: int) -> None:

    for i in range(1, n + 1):

        # print *
        for j in range(1, n + 1):

            if i == 1 or i == n or j == 1 or j == n:
                print('*', end='')
            else:
                print(' ', end='')
        print()


print_triangle(5)
