# 1
# 12
# 123
# 1234
# 12345

# prints the above pattern

def print_number_triangle(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


print_number_triangle(5)

