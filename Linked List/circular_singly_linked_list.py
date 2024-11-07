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
        :return: The new length of the linked list.
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

        return self.length

    def prepend(self, value):
        """
        Adds a new node with the given value to the beginning of the linked list.

        :param value: The value of the new node.
        :return: The new length of the linked list.
        """

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        self.length += 1

        return self.length

    def insert_at_index(self, index, value):
        """
        Inserts a new node with the given value at the specified index in the linked list.

        :param index: The position at which to insert the new node.
        :param value: The value of the new node.
        :return: The new length of the linked list.
        """

        if index < 0 or index > self.length:
            return self.length

        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp_node = self.head

        for _ in range(index - 1):
            temp_node = temp_node.next

        new_node.next = temp_node.next
        temp_node.next = new_node

        self.length += 1

        return self.length

    def traverse(self):
        """
        Traverse and print the values of all nodes in the linked list.
        """

        temp_node = self.head

        while temp_node is not None:
            print(temp_node.value, end=' ')
            temp_node = temp_node.next

            if temp_node == self.head:
                break

        print()

    def search(self, value):
        """
        Check if the given value is present in the linked list.

        :param value: The value to search for.
        :return: True if the value is found, False otherwise.
        """

        temp_node = self.head

        while temp_node is not None:
            if temp_node.value == value:
                return True
            temp_node = temp_node.next

            if temp_node == self.head:
                break

        return False

    def get_node_at_index(self, index):
        """
        Retrieve the node at the specified index in the linked list.

        :param index: The position of the node to retrieve.
        :return: The node at the specified index, or None if the index is invalid.
        """

        if index < 0 or index >= self.length:
            return None

        if index == self.length - 1 or index == -1:
            return self.tail

        temp_node = self.head

        for _ in range(index):
            temp_node = temp_node.next

        return temp_node

    def set_value_at_index(self, index, new_value):
        """
        Set the value of the node at the specified index in the linked list.

        :param index: The position of the node to set the value for.
        :param new_value: The new value for the node.
        :return: True if the index is valid, False otherwise.
        """

        temp_node = self.get_node_at_index(index)

        if temp_node:
            temp_node.value = new_value
            return True

        return False

    def pop_first(self):
        """
        Remove and return the first node from the linked list.

        :return: The value of the first node, or None if the linked list is empty.
        """

        if self.length == 0:
            return None

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None

        self.length -= 1

        return popped_node.value

    def pop(self):
        """
        Remove and return the last node from the linked list.

        :return: The value of the last node, or None if the linked list is empty.
        """

        if self.length == 0:
            return None

        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head

            while temp_node.next is not self.tail:
                temp_node = temp_node.next

            temp_node.next = self.head
            self.tail = temp_node
            popped_node.next = None

        self.length -= 1

        return popped_node.value

    def remove_at_index(self, index):
        """
        Remove and return the node at the specified index from the linked list.

        :param index: The position of the node to remove.
        :return: The value of the removed node, or None if the index is invalid.
        """

        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        elif index == self.length - 1 or index == -1:
            return self.pop()

        previous_node = self.get_node_at_index(index - 1)

        if previous_node:
            popped_node = previous_node.next
            previous_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node.value

        return None

    def delete_all(self):
        """
        Remove all nodes from the linked list.
        """

        if self.length == 0:
            return None

        self.tail.next = None  # This line is necessary to avoid circular references when the list is empty.
        self.head = None
        self.tail = None
        self.length = 0

