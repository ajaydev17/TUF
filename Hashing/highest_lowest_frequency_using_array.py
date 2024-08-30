def count_frequency(numbers):
    visited = [False] * len(numbers)
    max_element = 0
    max_frequency = 0
    min_element = 0
    min_frequency = len(numbers)
    for i in range(len(numbers)):
        if visited[i]:
            continue
        count = 1
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                count = count + 1
                visited[j] = True

        if count > max_frequency:
            max_element = numbers[i]
            max_frequency = count

        if count < min_frequency:
            min_element = numbers[i]
            min_frequency = count

    print(f"Max frequency element: {max_element}, min frequency element: {min_element}")


count_frequency([1, 2, 2, 3, 1, 4])
