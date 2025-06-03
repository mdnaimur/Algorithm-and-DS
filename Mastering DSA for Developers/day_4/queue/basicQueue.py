class BasicQueue:
    def __init__(self, capacity=5):
        self.__capacity = capacity
        self.queue = [None] * capacity
        self.__size = 0

    def enQueue(self, data):
        if self.__isFull():
            raise Exception("Queue is Full")
            # return print("Queue is Full..... remove first...")

        self.queue[self.__size] = data
        self.__size += 1
        # print("[DEBUG enQueue Size]: ", self.__size)

    def deQueue(self):
        if self.__isEmpty():
            raise Exception("Your Queue is Empty.....Add first ")

        front = self.queue[0]
        for i in range(1, self.__size):
            # print("[DEBUG dequeue i value] ", i-1)
            self.queue[i-1] = self.queue[i]

        self.queue[self.__size - 1] = None
        self.__size -= 1
        return front

    def peek(self):
        # print("[Peek: size ]", self.__size)
        return self.queue[0] if self.queue else None

    def __isEmpty(self):
        return self.__size == 0

    def __isFull(self):
        return self.__size == self.__capacity

    def __str__(self):
        return str(self.queue[:self.__size])


queue = BasicQueue()

# print(queue.__isFull())
queue.enQueue(10)
queue.enQueue(20)
queue.enQueue(30)
queue.enQueue(40)
queue.enQueue(50)

print(queue)
print("Dequeue item: ", queue.deQueue())
print("Peek item:", queue.peek())
