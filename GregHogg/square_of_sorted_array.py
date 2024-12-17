# square of a sorted array using two pointers approach
# time complexity O(n) and space complexity O(n)

def square_sorted_array(nums):
    result = [0] * len(nums)
    left, right = 0, len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1

    return result