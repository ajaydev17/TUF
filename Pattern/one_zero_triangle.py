# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

# prints the above pattern

def print_triangle(n: int) -> None:
    value = 1

    for i in range(0, n):
        if i % 2 == 0:
            value = 1
        else:
            value = 0

        for _ in range(0, i + 1):
            print(value, end=' ')

            value = 1 - value

        print()


print_triangle(5)
