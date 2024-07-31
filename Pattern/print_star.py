# *****
# *****
# *****
# *****
# *****

# prints the above pattern

def print_star(n: int) -> None:
    for _ in range(n):
        for _ in range(n):
            print("*", end="")
        print()


print_star(5)
