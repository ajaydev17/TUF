# three sum brute force approach, using three for loops
# one starts from i=0 and another one starts from j=i+1 and another one from k=j+1
# time complexity is O(n^2) and space complexity is O(1)

def three_sum_brute_force(nums):
    st = set()

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    st.add(tuple(temp))

    result = [list(item) for item in st]

    return result


# three sum using better solution
# we use hashset, using two loop
# time complexity is O(n^2) and space complexity is O(n)

def three_sum_better(nums):

    for i in range(len(nums)):
        hash_set = set()

        for j in range(i+1, len(nums)):
            complement = - (nums[i] + nums[j])

            if complement in hash_set:
                temp = [nums[i], nums[j], complement]
                temp.sort()
                hash_set.add(tuple(temp))

            hash_set.add(nums[j])

        result = [list(item) for item in hash_set]

        return result

# three sum using optimal solution
# sort the array start an index i=0, j=i+1 and k=n-1
# time complexity is O(n*logn) and space complexity is O(1)

def three_sum_optimal(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1

    return result
