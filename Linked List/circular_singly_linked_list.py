# node definition

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


# linked list definition

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
