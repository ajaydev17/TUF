def left_rotate_array(arr, k):
    k = k % len(arr)

    temp = arr[:k]

    for i in range(k, len(arr)):
        arr[i - k] = arr[i]

    for j in range(len(arr) - k, len(arr)):
        arr[j] = temp[j - len(arr) + k]


my_array = [1, 2, 3, 4, 5, 6]
k = 5
left_rotate_array(my_array, k)
print(my_array)
