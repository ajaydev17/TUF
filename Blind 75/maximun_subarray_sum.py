# maximum subarray sum using brute force
# use three loops
# time complexity is O(n*3) and space complexity is O(1)

def max_subarray_brute_force(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_sum = 0

            for k in range(i, j + 1):
                current_sum = current_sum + nums[k]

            max_sum = max(max_sum, current_sum)

    return max_sum

# maximum subarray sum using better solution
# use two loops
# time complexity is O(n*2) and space complexity is O(1)

def max_subarray_better_solution(nums):
    max_sum = float('-inf')

    for i in range(len(nums)):
        current_sum = 0

        for j in range(i, len(nums)):
            current_sum = current_sum + nums[j]

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

# maximum subarray sum using Kadane's algorithm
# using one loop
# time complexity O(n) and space complexity is O(1)

def max_subarray_kadane(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

# follow up question print the subarray

def max_subarray_print(nums):
    max_sum = float('-inf')
    current_sum = 0

    start = 0
    start_index = 0
    end_index = 0

    for i in range(len(nums)):

        if current_sum == 0:
            start = i

        current_sum = current_sum + nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = start
            end_index = i

        if current_sum < 0:
            current_sum = 0