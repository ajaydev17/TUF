from typing import List

def get_max_element(numbers: List[int]) -> int:

    # initialize a variable with a min value
    max_element = float('-inf')

    # iterate through the list to find the max element
    for index, value in enumerate(numbers):
        max_element = max(max_element, value)

    # return the max element
    return max_element

# time complexity: O(n)
# space complexity: O(1)