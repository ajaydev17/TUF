def find_largest_element(arr):
    largest = arr[0]

    for i in range(1, len(arr)):
        largest = max(arr[i], largest)

    return largest


my_array = [13, 46, 24, 52, 20, 9]
largest_element = find_largest_element(my_array)
print(f"Largest element is: {largest_element}")
