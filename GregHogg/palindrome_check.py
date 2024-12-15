# brute force by reversing the string
# time complexity O(n) and space complexity O(n)

def palindrome_check_brute_force(my_str):
    # reverse the string
    reversed_str = my_str[::-1]

    # compare the original string with the reversed string
    if my_str == reversed_str:
        return True
    else:
        return False


# better solution using two pointers
# time complexity O(n) and space complexity O(1)

def palindrome_check_better(my_str):
    # initialize pointers at the beginning and end of the string respectively
    left = 0
    right = len(my_str) - 1

    # compare characters from both ends of the string until they meet in the middle or cross each other
    while left < right:
        # if characters are not equal, the string is not a palindrome
        if my_str[left] != my_str[right]:
            return False

        # move the pointers towards each other
        left += 1
        right -= 1

    return True

# optimized solution input contains non-alphanumeric characters
# time complexity O(n) and space complexity O(n)

def palindrome_check_optimized(my_str):
    # remove non-alphanumeric characters
    my_str = ''.join(filter(str.isalnum, my_str)).lower()

    # initialize pointers at the beginning and end of the string respectively
    left = 0
    right = len(my_str) - 1

    # compare characters from both ends of the string until they meet in the middle or cross each other
    while left < right:
        # if characters are not equal, the string is not a palindrome
        if my_str[left] != my_str[right]:
            return False

        # move the pointers towards each other
        left += 1
        right -= 1

    return True