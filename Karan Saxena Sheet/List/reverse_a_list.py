from typing import List

def list_reverse(numbers: List[int]) -> int:

    # initialize two variables with start and end index
    left = 0
    right = len(numbers) - 1

    # iterate through the numbers for swapping the elements
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]

        # decrement and increment right, left after reach repeating
        right = right - 1
        left = left + 1

    # return the original list
    return numbers

# time complexity: O(n)
# space complexity: O(1)