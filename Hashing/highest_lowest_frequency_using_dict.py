def count_frequency(numbers):
    count = {}

    for number in numbers:
        if number in count:
            count[number] = count[number] + 1
        else:
            count[number] = 1

    max_element = 0
    max_frequency = 0
    min_element = 0
    min_frequency = len(numbers)

    for index, (key, value) in enumerate(count.items()):
        count = value
        element = key

        if count > max_frequency:
            max_element = element
            max_frequency = count

        if count < min_frequency:
            min_element = element
            min_frequency = count

    print(f"Max frequency element: {max_element}, min frequency element: {min_element}")


count_frequency([1, 2, 2, 3, 1, 4])