# node definition

class Node:
    """
    Node class to represent a single node in a linked list.
    """

    def __init__(self, value):
        """
        Initialize a new node with the given value.

        :param value: The value to be stored in the node.
        """

        self.value = value
        self.next = None

    def __str__(self):
        """
        Return a string representation of the node.

        :return: A string containing the node's value.
        """

        return str(self.value)


# linked list definition

class LinkedList:
    """
    Linked list class to store a collection of nodes.
    """

    def __init__(self):
        """
        Initialize an empty linked list with a head and tail pointer.

        :return: A new linked list object.
        """

        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """
        Return a string representation of the linked list.

        :return: A string containing the values of all nodes in the linked list.
        """

        result = ''
        temp_node = self.head

        while temp_node is not None:
            result = result + str(temp_node.value)
            temp_node = temp_node.next

            if temp_node == self.head:
                break

            result = result +' -> '

        return result

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.

        :param value: The value to be stored in the new node.
        """

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1
