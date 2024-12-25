# recursive approach
# time complexity O(n * n!) and space complexity O(n * n!)

def generate_permutations(s):
    # Base case
    if len(s) == 1:
        return [s]

    # recursive case

    # initialize the permutation list
    permutations = []

    # iterate through the string
    for i in range(len(s)):
        # get the first character
        char = s[i]

        # get the remaining characters
        remaining_chars = s[:i] + s[i+1:]

        # generate the permutations for the remaining characters
        for perm in generate_permutations(remaining_chars):
            # add the first character to the beginning of each permutation
            permutations.append(char + perm)

    # return the permutations
    return permutations
