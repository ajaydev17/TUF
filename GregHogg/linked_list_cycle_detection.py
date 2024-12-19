# linked list cycle detection using a set
# time complexity O(n) and space complexity O(n)

def has_cycle(head):
    # initialize a set
    seen = set()

    # a current node which points to head
    current = head

    while current:
        # if the current node is already in the set, it means there is a cycle
        if current in seen:
            return True

        # add the current node to the set
        seen.add(current)

        # move to the next node
        current = current.next

    # if the loop ends without finding a cycle, return False
    return False