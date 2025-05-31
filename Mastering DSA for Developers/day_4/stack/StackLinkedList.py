class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self, max_size=10):
        self.top = None
        self.maxSize = max_size
        self.size = 0

    def push(self, data):
        if self.is_full():
            raise Exception("Stack Overflow")

        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")

        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        return self.top.data

    def is_full(self):
        return self.size >= self.maxSize

    def is_empty(self):
        return self.size == 0

    def getSize(self):
        return self.size

    def clear(self):
        self.top = None
        self.size = 0

    def print_stack(self):
        current = self.top
        result = ''
        while current:
            result += f"{current.data}" + (" --> " if current.next else "")
            current = current.next
        return result

    def __str__(self):
        current = self.top
        values = []
        while current:
            values.append(current.data)
            current = current.next
        return f"Stack: {values}"


stack = StackLinkedList()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)

stack.push(10)
stack.push(11)

print(stack.print_stack())
print("size ", stack.getSize())
# print("Clear", stack.clear())
# print("size ", stack.getSize())
# print(stack)


print("pop:", stack.pop())
print("peek:", stack.peek())
print("pop:", stack.pop())
print("pop:", stack.pop())
print("pop:", stack.pop())
print("pop:", stack.pop())
print("pop:", stack.pop())
print("pop:", stack.pop())
print(stack)
