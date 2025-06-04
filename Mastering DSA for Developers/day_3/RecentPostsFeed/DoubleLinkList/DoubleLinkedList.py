from DoubleLinkList.Node import Node


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # TODO preRemove()

    def pop_front(self):
        if not self.head:
            return None

        current = self.head
        self.head = current.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1

    def remove(self, data):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.data != data:
                current = current.next
                continue

            if current == self.head and current == self.tail:
                self.head = None
                self.tail = None
                self.size -= 1
                return True

            if current == self.head:
                self.head = current.next
                if self.head:
                    self.head.prev = None
                self.size -= 1
                return True

            if current == self.tail:
                self.tail = current.prev
                if self.tail:
                    self.tail.next = None
                self.size -= 1
                return True

# print and string
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
