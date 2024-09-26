def linear_search(arr, target):

    for index in range(len(arr)):
        if arr[index] == target:
            return index

    return -1


my_array = [1, 2, 3, 4, 5]
target = 5

found_index = linear_search(my_array, target)

if found_index == -1:
    print(f"Element {target} not found in the list.")
else:
    print(f"Element found at index {int(found_index) + 1}")
