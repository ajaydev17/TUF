#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

# prints the above pattern

def print_triangle(n: int) -> None:
    space = n - 1

    for i in range(1, n + 1):

        # print space
        for _ in range(1, space + 1):
            print(' ', end='')

        # print alphabet
        for j in range(0, i):
            alphabet = chr(65 + j)
            print(alphabet, end='')

        for j in range(i - 2, -1, -1):
            alphabet = chr(65 + j)
            print(alphabet, end='')

        # print space
        for _ in range(1, space + 1):
            print(' ', end='')

        space = space - 1

        print()


print_triangle(5)