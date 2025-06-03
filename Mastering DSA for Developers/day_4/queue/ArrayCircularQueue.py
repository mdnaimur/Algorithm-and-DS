class ArrayCircularQueue:
    def __init__(self, size=10):
        self.queue = [None] * size
        self.size = size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, data):
        if self.isFull():
            raise Exception("Queue is Full...")

        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size
        print("[DEBUG rear size]", self.rear)
        self.count += 1

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty....")

        value = self.queue[self.front]
        # It alwayes look like it.. no need to write code here
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1

        return value

    def peek(self):
        return self.queue[self.front] if self.queue else None

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def __str__(self):
        if self.isEmpty():
            return "Queue is Empty"
        result = []
        index = self.front
        for _ in range(self.count):
            result.append(str(self.queue[index]))
            index = (index + 1) % self.size
        return " <- ".join(result)


q = ArrayCircularQueue(30)
for i in range(10, 30):
    q.enQueue(i)

print("Queue ", q)
print("Dequeue ", q.deQueue())
print("Peek  ", q.peek())
print("Update Queue ", q)
print("Dequeue ", q.deQueue())
print("Update Queue ", q)
print("Dequeue ", q.deQueue())
print("Update Queue ", q)
print("Dequeue ", q.deQueue())
print("Update Queue ", q)
print("Dequeue ", q.deQueue())
print("Update Queue ", q)
