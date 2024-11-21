# brute force approach using two loops
# time complexity O(n*2) and space complexity O(n)

def product_except_self(nums):
    result = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result.append(product)

    return result


# better approach by division
# time complexity O(n) and space complexity O(n)

def product_except_self_better(nums):
    total_product = 1
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num

    result = []

    for num in nums:
        if zero_count > 1:
            result.append(0)
        elif zero_count == 1:
            result.append(total_product if num == 0 else 0)
        else:
            result.append(total_product // num)

    return result


# optimal solution using prefix and suffix product
# time complexity O(n) and space complexity O(n)

def product_except_self_optimal(nums):
    n = len(nums)
    result = [1] * n
    prefix_product = 1
    suffix_product = 1

    for i in range(n):
        result[i] *= prefix_product
        prefix_product *= nums[i]

    for i in range(n-1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]

    return result