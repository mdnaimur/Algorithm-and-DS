class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self, max_size=10):
        self.top = None
        self.maxSize = max_size
        self.size = 0  # Track current size of stack

    def push(self, data):
        if self.is_full():
            raise Exception("Stack Overflow")

        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1  # ✅ Update size

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")

        data = self.top.data
        self.top = self.top.next
        self.size -= 1  # ✅ Update size
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        return self.top.data

    def is_full(self):
        return self.size >= self.maxSize  # ✅ Use self.size instead of self.top

    def is_empty(self):
        return self.size == 0  # ✅ Proper check for empty stack

    def __str__(self):
        current = self.top
        values = []
        while current:
            values.append(current.data)
            current = current.next
        return f"Stack (top to bottom): {values}"

    def print_stack(self):
        current = self.top
        result = ''
        while current:
            result += f"{current.data}" + (" -> " if current.next else "")
            current = current.next
        print(result)
