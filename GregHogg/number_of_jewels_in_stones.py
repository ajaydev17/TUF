# time complexity O(n + m) and space complexity O(1)

def number_of_jewels_in_stones(jewels, stones):
    # convert jewels to a set for faster lookup
    jewel_count = 0
    jewel_set = set(jewels)

    # count the number of jewels in the stones by checking if each stone is in the jewel set
    for stone in stones:
        if stone in jewel_set:
            jewel_count += 1

    return jewel_count