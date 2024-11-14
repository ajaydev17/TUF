# two sum brute force approach, using two for loops
# one starts from i=0 and another one starts from j=i+1
# time complexity is O(n^2) and space complexity is O(1)

def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# two sum using better approach using hashmap
# subtract the elements from target and check that value present in hashmap if present return indexes
# time complexity is O(n) and space complexity is O(n)

def two_sum_better(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_dict:
            return [num_dict[complement], i]

        num_dict[num] = i

    return []


# two sum using two pointers approach
# the array should be sorted
# take one pointer from left=0 and another from right=n-1, if sum less than target increase left pointer and if sum greater than target decrease right
# time complexity is O(n*logn) and space complexity is O(n)

def two_sum_two_pointer(nums, target):
    nums = sorted(nums)

    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []
