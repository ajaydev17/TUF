def find_subarray(arr, k):
    left = 0
    right = 0
    max_len = 0

    res = arr[0]

    while right < len(arr):

        while left <= right and res > k:
            res = res - arr[left]
            left = left + 1

        if res == k:
            max_len = max(max_len, right - left + 1)

        right = right + 1

        if right < len(arr):
            res = res + arr[right]

    return max_len


arr = [-1, 1, 1]
k = 0
result = find_subarray(arr, k)
print(f"Max length sub array is: {result}")
