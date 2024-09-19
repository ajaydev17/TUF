def find_second_largest(arr):
    if len(arr) < 2:
        return -1

    largest = float('-inf')
    second_largest = float('-inf')

    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] != largest and arr[i] > second_largest:
            second_largest = arr[i]

    return second_largest


my_array = [13, 46, 24, 52, 20, 9]
second_largest_element = find_second_largest(my_array)
print(f"Second largest element is: {second_largest_element}")