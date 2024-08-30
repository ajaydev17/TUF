def count_frequency(numbers):
    count = {}

    for number in numbers:
        if number in count:
            count[number] = count[number] + 1
        else:
            count[number] = 1

    print(count)


count_frequency([1, 2, 2, 3, 1, 4])