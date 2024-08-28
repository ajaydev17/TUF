def calculate_count():
    string = input('Enter the string: ')

    count_array = [0] * 26

    for index, char in enumerate(string):
        count_array[ord(char) - ord('a')] = count_array[ord(char) - ord('a')] + 1

    query = int(input('Enter the number of queries: '))

    while query:
        query_char = input('Enter the query character: ')
        print(count_array[ord(query_char) - ord('a')])
        query = query - 1


calculate_count()
