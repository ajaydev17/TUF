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


# Iterative approach
# time complexity O(n * n!) and space complexity O(n * n!)

def generate_permutations_iterative(s):
    # store the list and index in a stack
    stack = [(list(s), 0)]

    # initialize the result list
    result = []

    while stack:
        # pop a permutation and its index from the stack
        permutation, index = stack.pop()

        # if the index is equal to the length of the permutation, add it to the result list
        if index == len(permutation):
            result.append(''.join(permutation))
        else:
            # iterate through the remaining characters
            for i in range(index, len(permutation)):
                # swap the current character with the character at the index
                permutation[i], permutation[index] = permutation[index], permutation[i]

                # push the updated permutation and its index to the stack
                stack.append((permutation, index + 1))

                # swap the characters back to restore the original permutation
                permutation[i], permutation[index] = permutation[index], permutation[i]

    # return the permutation
    return result
