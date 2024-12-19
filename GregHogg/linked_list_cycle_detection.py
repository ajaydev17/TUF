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

# linked list cycle detection using two pointer
# time complexity O(n) and space complexity O(1)

def has_cycle_two_pointer(head):
    # initialize two pointers, slow and fast
    slow = head
    fast = head

    while fast and fast.next:
        # move slow pointer one step at a time
        slow = slow.next

        # move fast pointer two steps at a time
        fast = fast.next.next

        # if the two pointers meet, it means there is a cycle
        if slow == fast:
            return True

    # if the loop ends without finding a cycle, return False
    return False