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