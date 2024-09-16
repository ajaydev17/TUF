def recursive_bubble_sort(arr, n):

    if n == 1:
        return

    for j in range(n - 1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    recursive_bubble_sort(arr, n - 1)


my_array = [13, 46, 24, 52, 20, 9]
recursive_bubble_sort(my_array, len(my_array))
print(my_array)
