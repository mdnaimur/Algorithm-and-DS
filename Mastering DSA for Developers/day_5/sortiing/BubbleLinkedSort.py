class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class BubbleLinkedListSort:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def sortBubble(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def printList(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        print(" --> ".join(values))


li = BubbleLinkedListSort()
li.append(4)
li.append(2)
li.append(5)
li.append(1)
li.append(3)
print(li)
print("Before sorting")
li.printList()
li.sortBubble()
print("After sorting")
li.printList()
