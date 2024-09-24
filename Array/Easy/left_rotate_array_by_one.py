def left_rotate_array(arr):
    temp = arr[0]

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]

    arr[len(arr) - 1] = temp


my_array = [1, 2, 3, 4, 5, 6]
left_rotate_array(my_array)
print(my_array)
