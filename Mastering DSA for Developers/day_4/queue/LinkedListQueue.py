class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, data):

        newNode = Node(data)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def deQueue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        return self.front.value if self.front else None

    def isEmpty(self):
        return self.front is None

    def __str__(self):
        values = []
        current = self.front
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Queue is Empty"


queue = LinkedListQueue()

# print(queue.__isFull())
queue.enQueue(10)
queue.enQueue(20)
queue.enQueue(30)
queue.enQueue(40)
queue.enQueue(50)


print("Queue:", queue)
print("Dequeue item: ", queue.deQueue())
print("Queue after dequeue:", queue)
print("Peek item:", queue.peek())
