# A
# A B
# A B C
# A B C D
# A B C D E


# prints the above pattern

def print_triangle(n: int) -> None:

    for i in range(0, n):

        for j in range(0, i + 1):
            alphabet = chr(65 + j)
            print(alphabet, end=' ')

        print()


print_triangle(5)