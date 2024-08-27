def string_palindrome_check(start, string):
    if start >= len(string) // 2:
        return True

    if string[start] != string[len(string) - start - 1]:
        return False

    return string_palindrome_check(start + 1, string)


start = 0
string = 'madam'

print(f'Is {string} palindrome: {string_palindrome_check(start, string)}')


# check palindrome using while loop
# def is_palindrome(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     left = 0
#     right = len(s) - 1
#
#     while left < right:
#         if not s[left].isalnum():
#             left = left + 1
#         elif not s[right].isalnum():
#             right = right - 1
#         elif s[left].lower() != s[right].lower():
#             return False
#         else:
#             left = left + 1
#             right = right - 1
#
#     return True
