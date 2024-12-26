# reversing the string using constant space
# time complexity O(n) and space complexity O(1)

def reverse_string(my_str):
    # initialize the left and right pointers
    left = 0
    right = len(my_str) - 1

    # swap characters from the left and right pointers until they meet in the middle
    while left < right:
        my_str[left], my_str[right] = my_str[right], my_str[left]
        left += 1
        right -= 1