def move_zeros_to_end(arr):

    j = -1

    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break

    if j == -1:
        return arr

    for k in range(j + 1, len(arr)):
        if arr[k] != arr[j]:
            arr[k], arr[j] = arr[j], arr[k]
            j = j + 1


my_array = [1, 2, 0, 3, 0, 0, 4, 0, 5]
move_zeros_to_end(my_array)
print(my_array)
