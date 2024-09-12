def insertion_sort(arr):
    for i in range(len(arr)):
        j = i

        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j - 1



my_array = [13, 46, 24, 52, 20, 9]
insertion_sort(my_array)
print(my_array)
