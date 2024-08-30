def count_frequency(numbers):
    visited = [False] * len(numbers)
    for i in range(len(numbers)):
        if visited[i]:
            continue
        count = 1
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                count = count + 1
                visited[j] = True

        print(f"number: {numbers[i]}, count: {count}")


count_frequency([1, 2, 2, 3, 1, 4])

