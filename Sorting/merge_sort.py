def do_sort(arr, low, mid, high):
    temp = []

    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left = left + 1
        else:
            temp.append(arr[right])
            right = right + 1


    while left <= mid:
        temp.append(arr[left])
        left = left + 1

    while right <= high:
        temp.append(arr[right])
        right = right + 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]


def merge_sort(arr, low, high):

    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    do_sort(arr, low, mid, high)



my_array = [13, 46, 24, 52, 20, 9]
merge_sort(my_array, 0, len(my_array) - 1)
print(my_array)
