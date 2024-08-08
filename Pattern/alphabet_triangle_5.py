# E
# D E
# C D E
# B C D E
# A B C D E

# prints the above pattern

def print_triangle(n: int) -> None:

    for i in range(0, n):

        for j in range(0, i + 1):
            alphabet = chr(65 + n - i + j - 1)
            print(alphabet, end=' ')

        print()


print_triangle(5)
