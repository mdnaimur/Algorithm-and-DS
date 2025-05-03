from .Node import Node


class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        # Event Driven
        self.on_insert = None
        self.on_update = None
        self.on_delete = None

    def set_on_insert(self, funcData):
        self.on_insert = funcData

    def set_on_update(self, funcData):
        self.on_update = funcData

    def set_on_delete(self, funcData):
        self.on_delete = funcData

    def insert(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        else:
            self.tail.next = new_node
            self.tail = new_node

        # Event Dirven Trigger
        if self.on_insert:
            self.on_insert(data)

    def preend(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

        if self.on_insert:
            self.on_insert(data)

    def update(self, data, postion):
        if postion < 0 or postion > self.size:
            return None

        if postion == 0:
            self.preend(data)
            return True

        new_node = Node(data)
        current = self.head
        previous = 0
        index = 0

        while index < postion:
            previous = current
            current = current.next
            index += 1

        new_node.next = current
        previous.next = new_node

        # Event Trigger on update
        if self.on_update:
            self.on_update(data)

        return True

    def delete(self, data):
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            # Event Trigger
            if self.on_delete:
                self.on_delete(data)
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                if not current.next:
                    self.tail = current
                  # Event Trigger
                if self.on_delete:
                    self.on_delete(data)
                return True
            current = current.next

        return False

    def to_arry(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return "--> ".join(str(x) for x in self.to_arry()) + "-->"
