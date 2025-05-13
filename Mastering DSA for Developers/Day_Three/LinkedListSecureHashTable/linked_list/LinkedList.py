from linked_list.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def remove(self, key):
        if not self.head:
            return

        if self.head.key == key:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current and current.key != key:
            previous = current
            current = current.next

        if current:
            previous.next = current.next

        return None

    def find(self, key):
        if not self.head:
            return None

        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def entries(self):
        current = self.head

        while current:
            yield (current.key, current.value)
            current = current.next
