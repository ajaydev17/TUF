def get_pivot_index(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:

        while arr[i] <= pivot and i <= high - 1:
            i = i + 1

        while arr[j] > pivot and j >= low + 1:
            j = j - 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = get_pivot_index(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


my_array = [13, 46, 24, 52, 20, 9]
quick_sort(my_array, 0, len(my_array) - 1)
print(my_array)
