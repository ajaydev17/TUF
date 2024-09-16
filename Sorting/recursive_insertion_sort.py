def recursive_insertion_sort(arr, i, n):

    if i == n:
        return

    j = i

    while j > 0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j = j - 1

    recursive_insertion_sort(arr, i + 1, n)



my_array = [13, 46, 24, 52, 20, 9]
recursive_insertion_sort(my_array, 0, len(my_array))
print(my_array)
