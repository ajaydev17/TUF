from typing import List

def move_zeros_to_end(numbers: List[int]) -> List[int]:

    non_zero_index = 0

    for i in range(numbers):
        if numbers[i] != 0:
            numbers[non_zero_index], numbers[i] = numbers[i], numbers[non_zero_index]
            non_zero_index += 1

    return numbers

# time complexity: O(n)
# space complexity: O(1)