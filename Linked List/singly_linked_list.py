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
        elif index < 0 or index >= self.length:
            return None
        elif index == 0:
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

    def pop_first(self):
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
