def print_name_n_times(number, name):
    if number == 0:
        return

    print(name)
    print_name_n_times(number - 1, name)


print_name_n_times(5, "ClutchGod")
