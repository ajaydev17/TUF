def get_single_element(arr):

    xor = 0

    for num in arr:
        xor = xor ^ num

    return xor


arr = [4, 1, 2, 1, 2]
ans = get_single_element(arr)
print("The single element is:", ans)