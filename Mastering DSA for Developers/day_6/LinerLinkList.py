class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def liner_search_linked_list(head, target):
    current = head
    index = 0
    while current is not None:
        if current.value == target:
            return index
        current = current.next
        index += 1

    return -1


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

target = 20
result = liner_search_linked_list(head, target)
print("Target found at index:", result)
