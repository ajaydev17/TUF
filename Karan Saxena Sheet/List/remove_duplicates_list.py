from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:

    # check base condition
    if len(numbers) <= 1:
        return numbers

    # initialize two pointers i and j
    i = 0
    j = 1

    while j < len(numbers):
        if numbers[i] != numbers[j]:
            i = i + 1
            numbers[i] = numbers[j]

        j = j + 1

    # return the numbers up to i
    return numbers[:i + 1]