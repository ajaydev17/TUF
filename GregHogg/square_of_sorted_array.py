# square of a sorted array using two pointers approach
# time complexity O(n) and space complexity O(n)

def square_sorted_array(nums):
    # initialize an empty list with zero values
    result = [0] * len(nums)

    # initialize pointers at the beginning and end of the string respectively
    left, right = 0, len(nums) - 1

    # iterate over the array in reverse order and calculate the square of each element
    for i in range(len(nums) - 1, -1, -1):

        # calculate the square of the element pointed by the left pointer if it's larger,
        # otherwise, calculate the square of the element pointed by the right pointer
        # and increment the pointers accordingly.
        # and add the value at corresponding index in result list
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1

    return result