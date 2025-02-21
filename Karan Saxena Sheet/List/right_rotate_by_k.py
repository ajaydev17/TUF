from typing import List

def rotate_list_by_k(arr: List[int], k: int) -> int:

    # get the k by modulo of arr length
    k = k % len(arr)

    # store the element that are moved by k
    temp = arr[:len(arr) - k]

    for i in range(len(arr) - k, len(arr)):
        arr[i - len(arr) + k] = arr[i]

    for j in range(k, len(arr)):
        arr[j] = temp[j - k]

    return arr

    # other way to do it
    # return arr[-k:] + arr[:-k]

# time complexity: O(n)
# space complexity: O(1)


