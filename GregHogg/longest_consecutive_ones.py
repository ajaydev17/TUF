# time complexity O(n * 2) and space complexity O(1)

def longest_consecutive_ones(nums, k):
    max_length, num_zeros, count = 0, 0, 0

    for index, value in enumerate(nums):
        if value == 0:
            num_zeros = num_zeros + 1

            while num_zeros > k:
                if nums[count] == 0:
                    num_zeros = num_zeros - 1
                count = count + 1

            length = index - count + 1
            max_length = max(max_length, length)

    return max_length