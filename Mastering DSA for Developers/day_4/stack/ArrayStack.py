class ArrayStack:
    def __init__(self, max_size=10):
        self.stack = [None] * max_size
        self.top = -1
        self.maxSize = max_size

    def push(self, value):
        if self.is_full():
            raise Exception('Stack overflow')
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        value = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack empty!!")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.maxSize - 1

    def show_stack(self):
        return str(self.stack)

    def __str__(self):
        return f"Stack: {self.stack[:self.top+ 1 ]}"


stack = ArrayStack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.show_stack())

print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print(stack)
