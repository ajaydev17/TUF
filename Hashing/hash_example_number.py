def calculate_count():
    numbers = input('Enter the numbers with space: ')
    numbers = numbers.split(' ')

    count_array = [0] * 13

    for index, number in enumerate(numbers):
        count_array[int(numbers[index])] = count_array[int(numbers[index])] + 1

    query = int(input('Enter the number of queries: '))

    while query:
        query_number = int(input('Enter the query number: '))
        print(count_array[query_number])
        query = query - 1


calculate_count()


