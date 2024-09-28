def count_max_consecutive_ones(arr):

    max_count = 0
    count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count = count + 1
        else:
            count = 0

        max_count = max(max_count, count)

    return max_count


nums = [1, 1, 0, 1, 1, 1]
count = count_max_consecutive_ones(nums)

print(f"The maximum  consecutive 1's are: {count}")