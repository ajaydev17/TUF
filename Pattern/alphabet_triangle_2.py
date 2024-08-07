# A B C D E
# A B C D
# A B C
# A B
# A


# prints the above pattern

def print_triangle(n: int) -> None:

    for i in range(0, n):

        for j in range(0, n - i):
            alphabet = chr(65 + j)
            print(alphabet, end=' ')

        print()


print_triangle(5)