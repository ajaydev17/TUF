# node definition

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


# linked list definition

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        temp_node = self.head

        while temp_node is not None:
            result = result + str(temp_node.value)

            if temp_node.next is not None:
                result = result + ' --> '
            temp_node = temp_node.next

        return result

    def append(self, value):
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
        if index < 1:
            return "Invalid index provided."

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head

            for _ in range(index - 1):
                temp_node = temp_node.next

            temp_node_next = temp_node.next
            new_node.next = temp_node_next
            temp_node.next = new_node

        self.length = self.length + 1

        return self.length

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head

        while current is not None:
            if current.value == target:
                return True
            current = current.next

        return False

    def get_node(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        elif index == 1:
            return self.head

        current = self.head
        for _ in range(index):
            current = current.next

        return current

    def set_value(self, index, value):
        temp = self.get_node(index)

        if temp:
            temp.value = value
            return True

        return False