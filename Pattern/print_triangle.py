# *
# **
# ***
# ****
# *****

# prints the above pattern
def print_triangle(n: int) -> None:
    for i in range(n):
        for _ in range(i + 1):
            print("*", end="")
        print()


print_triangle(5)
