# search in sorted 2D array using two pointers
# time complexity O(n) and space complexity O(1)

def search_in_sorted_2d_array(matrix, target):
    # check if the matrix is empty
    if not matrix or not matrix[0]:
        return False

    # calculate total number of elements in the matrix
    rows, cols = len(matrix), len(matrix[0])

    # initialize two pointers, left and right, to the top right corner of the matrix
    left, right = 0, rows * cols - 1

    # perform binary search until the left pointer is less than or equal to the right pointer
    while left <= right:

        # calculate the mid index and its corresponding row and column indices
        mid = (left + right) // 2
        i = mid // cols
        j = mid % cols

        # compare the target value with the value at the mid index
        m_value = matrix[i][j]

        # if the target value is found, return True
        # if the target value is less than the value at the mid index, move the right pointer to the left
        # if the target value is greater than the value at the mid index, move the left pointer to the right
        # if the target value is not found, return False at the end of the loop
        if target == m_value:
            return True
        elif target > m_value:
            left = mid + 1
        else:
            right = mid - 1

    return False