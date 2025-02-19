from typing import List

def is_list_sorted(numbers: List[int]) -> bool:

    # iterate through the list to check if it is sorted
    for index, value in enumerate(numbers):
        if index < len(numbers) - 1 and numbers[index] > numbers [index + 1]:
            return False

    # if iteration is successful we can conclude that array is sorted
    return True

# time complexity: O(n)
# space complexity: O(1)