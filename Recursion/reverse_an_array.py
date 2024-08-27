def reverse_an_array(left, right, numbers):
    if left >= right:
        return

    numbers[left], numbers[right - 1] = numbers[right - 1], numbers[left]

    reverse_an_array(left + 1, right - 1, numbers)


numbers = [1, 2, 3, 4, 5]
left = 0
right = len(numbers)

reverse_an_array(left, right, numbers)
print(numbers)
