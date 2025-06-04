from min_stack.Node import Node


class MinStack:
    def __init__(self, max_size=10):
        self.main_stack = None
        self.min_stack = None
        self.maxSize = max_size
        self.main_stack_size = 0
        self.min_stack_size = 0

    def push(self, value):
        if self.isFull():
            raise Exception("Main Stack Overflow")

        newMainData = Node(value)
        newMainData.next = self.main_stack
        self.main_stack = newMainData
        self.main_stack_size += 1
        # now check min stack
        self._pushToMinStack(value)
        # minData = self.getMin()
        # if not self.main_stack or value <= minData:
        #     newMinData = Node(value)
        #     newMinData.next = self.min_stack
        #     self.min_stack = newMinData
        #     self.min_stack_size += 1
        # else:
        #     newMinData = Node(minData)
        #     newMinData.next = self.min_stack
        #     self.min_stack = newMinData
        #     self.min_stack_size += 1

    def _pushToMinStack(self, value):
        if self.min_stack is None or value <= self.min_stack.data:
            newMinData = Node(value)

        else:
            newMinData = Node(self.min_stack.data)

        newMinData.next = self.min_stack
        self.min_stack = newMinData
        self.min_stack_size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("No data available")

        popped_main = self.main_stack.data
        self.main_stack = self.main_stack.next
        self.main_stack_size -= 1
        # pop min data
        popped_main = self.min_stack.data
        self.min_stack = self.min_stack.next
        self.min_stack_size -= 1
        return popped_main, popped_main

    def peek(self):
        if self.isEmpty():
            raise Exception("Main Stack Empty")
        return self.main_stack.data

    def getMin(self):
        if self.min_stack is None:
            raise Exception("No data available on min stack ")
        return self.min_stack.data

    def isFull(self):
        return self.min_stack_size >= self.maxSize

    def isEmpty(self):
        return self.min_stack_size == 0

    def clear(self):
        self.main_stack = None
        self.main_stack_size = 0
        self.min_stack = None
        self.min_stack_size = 0

    def __toStackToList(self, top):
        result = []
        current = top
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __str__(self):
        return (
            f"Main Stack(top to bottom): {self.__toStackToList(self.main_stack)}\n"
            f"Min Stack(Top to Bottom): {self.__toStackToList(self.min_stack)}\n"
            f"Current min:{self.getMin() if not self.isEmpty() else 'N/A'}\n"
        )
