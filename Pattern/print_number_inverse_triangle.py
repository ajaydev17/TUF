# 12345
# 1234
# 123
# 12
# 1

# prints the above pattern

def print_triangle(n: int) -> None:
    for i in range(0, n):
        for j in range(1, n - i + 1):
            print(j, end='')
        print()


print_triangle(5)
