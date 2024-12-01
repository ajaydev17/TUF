# search in the rotated sorted array linear solution
# time complexity is O(n) and space complexity is O(1)

def search_in_rotated_sorted_array(nums, target):
    for num in nums:
        if num == target:
            return True

    return False


# search in the rotated sorted array binary search solution
# time complexity is O(logn) and space complexity is O(1)

def search_in_rotated_sorted_array_binary(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return True

        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False