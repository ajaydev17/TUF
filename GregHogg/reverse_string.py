# reversing the string using constant space
# time complexity O(n) and space complexity O(1)

def reverse_string(my_str):
    left = 0
    right = len(my_str) - 1

    while left < right:
        my_str[left], my_str[right] = my_str[right], my_str[left]
        left += 1
        right -= 1