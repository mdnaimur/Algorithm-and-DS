class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        # ✅ Event Handlers (function placeholders)
        self.on_insert = None
        self.on_remove = None
        self.on_clear = None

    # ✅ Methods to set event handler functions
    def set_on_insert(self, func):
        self.on_insert = func

    def set_on_remove(self, func):
        self.on_remove = func

    def set_on_clear(self, func):
        self.on_clear = func

    def append(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        # 🔔 Trigger on_insert event
        if self.on_insert:
            self.on_insert(data)

    def remove(self, data):
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None

            # 🔔 Trigger on_remove event
            if self.on_remove:
                self.on_remove(data)
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                if not current.next:
                    self.tail = current

                # 🔔 Trigger on_remove event
                if self.on_remove:
                    self.on_remove(data)
                return True
            current = current.next

        return False

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

        # 🔔 Trigger on_clear event
        if self.on_clear:
            self.on_clear()

    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return " -> ".join(str(x) for x in self.to_array()) + " -> None"
