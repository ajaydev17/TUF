def selection_sort(arr):

    for i in range(len(arr)-1):
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            break


my_array = [13, 46, 24, 52, 20, 9]
selection_sort(my_array)
print(my_array)
