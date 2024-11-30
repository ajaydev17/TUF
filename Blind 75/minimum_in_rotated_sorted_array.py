# finding the minimum in rotated sorted array linear solution
# time complexity is O(n) and space complexity is O(1)

def find_min_rotated_sorted_array_linear(nums):
    min_element = float('inf')

    for num in nums:
        if num < min_element:
            min_element = num

    return min_element


# finding the minimum in rotated sorted array using binary search solution
# time complexity is O(logn) and space complexity is O(1)

def find_min_rotated_sorted_array_binary(nums):
    left, right = 0, len(nums) - 1
    min_element = float('inf')

    while left < right:
        mid = (left + right) // 2

        if nums[left] <= nums[mid]:
            min_element = min(min_element, nums[left])
            left = mid + 1
        else:
            min_element = min(min_element, nums[mid])
            right = mid - 1

    return min_element

# finding the minimum in rotated sorted array using binary search solution
# time complexity is O(logn) and space complexity is O(1)

def find_min_rotated_sorted_array_binary_optimized(nums):
    left, right = 0, len(nums) - 1
    min_element = float('inf')

    while left < right:
        mid = (left + right) // 2

        if nums[left] <= nums[right]:
            min_element = min(min_element, nums[left])
            break

        if nums[left] <= nums[mid]:
            min_element = min(min_element, nums[left])
            left = mid + 1
        else:
            min_element = min(min_element, nums[mid])
            right = mid - 1

    return min_element