# array contains duplicates using brute force
# one variable starts from i=0 and other one starts from i+1
# time complexity O(n*2) and space complexity O(1)

def contains_duplicates_brute_force(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# array contains duplicates using better solution
# sort the array and compare the adjacent variables
# time complexity O(n*logn) and space complexity O(1)

def contains_duplicates_optimized(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# array contains duplicates using hash set optimal solution
# check if the element already present in the array if yes return True else add to hash set
# time complexity O(n) and space complexity O(n)

def contains_duplicates_hash_set(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False