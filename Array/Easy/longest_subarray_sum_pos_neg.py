def find_subarray(arr, k):

    pre_sum = {}
    max_len = 0
    arr_sum = 0

    for i in range(len(arr)):
        arr_sum = arr_sum + arr[i]

        if arr_sum == k:
            max_len = max(max_len, i + 1)

        rem_sum = k - arr_sum

        if rem_sum in pre_sum:
            length = i - pre_sum[rem_sum]
            max_len = max(max_len, length)

        if arr_sum not in pre_sum:
            pre_sum[arr_sum] = i

    return max_len


arr = [2, 0, 0, 3]
k = 3

result = find_subarray(arr, k)
print(f"Max length sub array is: {result}")