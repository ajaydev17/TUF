from typing import List

def list_sum(numbers: List[int]) -> int:

    # initialize a variable with sum 0
    result = 0

    # iterate through the list to find the sum
    for index, value in enumerate(numbers):
        result = result + value

    # return the sum
    return result

# time complexity: O(n)
# space complexity: O(1)