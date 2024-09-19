def remove_duplicates(arr):
    i = 0

    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i = i + 1
            arr[i] = arr[j]

    return arr[:i + 1]


my_array = [13, 13, 20, 46, 46, 50]
my_array = remove_duplicates(my_array)
print(my_array)
