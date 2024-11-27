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

# maximum subarray product using better solution
# use two loops
# time complexity is O(n*2) and space complexity is O(1)

def max_subarray_better_solution(nums):
    max_product = float('-inf')

    for i in range(len(nums)):
        current_product = 1
        for j in range(i, len(nums)):
            current_product = current_product * nums[j]
            max_product = max(max_product, current_product)

    return max_product

# maximum subarray product using optimal solution
# using prefix product and suffix product
# time complexity is O(n) and space complexity is O(1)

def max_subarray_optimal_solution(nums):
    max_product = float('-inf')
    prefix_product = 1
    suffix_product = 1

    for i in range(len(nums)):
        if prefix_product == 0:
            prefix_product = 1

        if suffix_product == 0:
            suffix_product = 1

        prefix_product = prefix_product * nums[i]
        suffix_product = suffix_product * nums[len(nums) - i - 1]
        max_product = max(max_product, max(prefix_product, suffix_product))

    return max_product



