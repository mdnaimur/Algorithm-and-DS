import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SelectionSortLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def selection_sort(self):
        if not self.head or not self.head.next:
            return
        current = self.head

        while current:
            minNode = current
            nextNode = current.next

            while nextNode:
                if nextNode.value < minNode.value:
                    minNode = nextNode
                nextNode = nextNode.next

            if minNode != current:
                current.value, minNode.value = minNode.value, current.value

            current = current.next

    def print_list(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" --> ".join(values))


# Example usage
def generate_random_array(length=10000):
    return [random.randint(1, 100) for _ in range(length)]


linked_list = SelectionSortLinkedList()
arr = generate_random_array(20)

for value in arr:
    linked_list.append(value)

print("Before Sorting:")
linked_list.print_list()

linked_list.selection_sort()

print("\nAfter Sorting:")
linked_list.print_list()
