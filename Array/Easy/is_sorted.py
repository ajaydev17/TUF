def is_sorted(arr):
    if len(arr) < 2:
        return True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False

    return True


my_array = [3, 4, 5, 1, 2]
is_array_sorted = is_sorted(my_array)
print(f'is array sorted: {is_array_sorted}')
