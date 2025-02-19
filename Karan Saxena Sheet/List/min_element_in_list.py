from typing import List

def get_min_element(numbers: List) -> int:

    # initialize a  variable with max value
    min_element = float('inf')

    # iterate through the list to find the min element
    for index, value in enumerate(numbers):
        min_element = min(min_element, value)

    # return the min element
    return min_element

# time complexity: O(n)
# space complexity: O(1)