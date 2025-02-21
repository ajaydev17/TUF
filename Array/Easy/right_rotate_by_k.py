def right_rotate_array(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    k = k % len(nums)

    temp = nums[:len(nums) - k]

    for i in range(len(nums) - k, len(nums)):
        nums[i - len(nums) + k] = nums[i]

    for j in range(k, len(nums)):
        nums[j] = temp[j - k]


my_array = [-1,-100,3,99]
k_rotate = 2
right_rotate_array(my_array, k_rotate)
print(my_array)
