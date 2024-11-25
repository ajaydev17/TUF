# maximum subarray product using brute force
# use three loops
# time complexity is O(n*3) and space complexity is O(1)
from itertools import product


def max_subarray_brute_force(nums):
    max_product = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_product = 1

            for k in range(i, j + 1):
                current_product = current_product * nums[k]

            max_product = max(max_product, current_product)

    return max_product