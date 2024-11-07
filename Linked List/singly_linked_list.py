# node definition

class Node:
    """
    Node class representing a single node in a linked list.
    """

    def __init__(self, value):
        """
        Initializes a new node with the given value.

        :param value: The value of the node.
        """

        self.value = value
        self.next = None


# linked list definition

class LinkedList:
    """
    Linked List class representing a linked list of nodes.
    """

    def __init__(self):
        """
        Initializes an empty linked list with a head and tail node.
        """

        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """
        Returns a string representation of the linked list.

        :return: A string containing the values of the nodes in the linked list, separated by ' --> '.
        """

        result = ''
        temp_node = self.head

        while temp_node is not None:
            result = result + str(temp_node.value)

            if temp_node.next is not None:
                result = result + ' --> '
            temp_node = temp_node.next

        return result

    def append(self, value):
        """
        Adds a new node with the given value to the end of the linked list.

        :param value: The value of the new node.
        :return: The new length of the linked list.
        """

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length = self.length + 1

        return self.length

    def prepend(self, value):
        """
        Adds a new node with the given value to the beginning of the linked list.

        :param value: The value of the new node.
        :return: The new length of the linked list.
        """

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length = self.length + 1

        return self.length

    def insert(self, value, index):
        """
        Inserts a new node with the given value at the specified index in the linked list.

        :param value: The value of the new node.
        :param index: The position at which to insert the new node.
        :return: The new length of the linked list.
        """

        if index < 1 or index > self.length:
            return "Invalid index provided."

        new_node = Node(value)

        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        else:
            temp_node = self.head

            for _ in range(index - 1):
                temp_node = temp_node.next

            temp_node_next = temp_node.next
            new_node.next = temp_node_next
            temp_node.next = new_node

            if new_node.next is None:
                self.tail = new_node

        self.length = self.length + 1

        return self.length

    def traverse(self):
        """
        Prints the values of the nodes in the linked list.
        """

        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        """
        Checks if the given value is present in the linked list.
        :param target: value to search for in the linked list.
        :return: True if the target is found, False otherwise.
        """

        current = self.head

        while current is not None:
            if current.value == target:
                return True
            current = current.next

        return False

    def get_node(self, index):
        """
        Returns the node at the specified index in the linked list.

        :param index: The index of the node to retrieve.
        :return: The node at the specified index or None if the index is invalid.
        """

        if index == -1:
            return self.tail
        elif index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.head

        current = self.head
        for _ in range(index):
            current = current.next

        return current

    def set_value(self, index, value):
        """
        Sets the value of the node at the specified index in the linked list.

        :param index: The index of the node to set the value for.
        :param value: The new value for the node.
        :return: True if the index is valid, False otherwise.
        """

        temp = self.get_node(index)

        if temp:
            temp.value = value
            return True

        return False

    def pop_first(self):
        """
        Removes and returns the first node from the linked list.

        :return: The popped node or None if the linked list is empty.
        """

        if self.length == 0:
            return None

        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None

        self.length = self.length - 1

        return popped_node

    def pop(self):
        """
        Removes and returns the last node from the linked list.

        :return: The popped node or None if the linked list is empty.
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

            temp_node.next = None
            self.tail = temp_node

        self.length = self.length - 1

        return popped_node

    def remove(self, index):
        """
        Removes and returns the node at the specified index from the linked list.

        :param index: The index of the node to remove.
        :return: The popped node or None if the index is invalid.
        """

        if index < -1 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == -1 or index == self.length - 1:
            return self.pop()

        prev_node = self.get_node(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None

        self.length = self.length - 1

        return popped_node
