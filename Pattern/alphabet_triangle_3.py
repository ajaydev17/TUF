# A
# B B
# C C C
# D D D D
# E E E E E


# prints the above pattern

def print_triangle(n: int) -> None:

    count = 0

    for i in range(0, n):

        for _ in range(0, i + 1):
            alphabet = chr(65 + count)
            print(alphabet, end=' ')

        count = count + 1

        print()


print_triangle(5)