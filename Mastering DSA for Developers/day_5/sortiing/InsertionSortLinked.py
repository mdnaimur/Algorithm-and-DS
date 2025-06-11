class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class InsertionSortLinkedList:
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

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        dummy = Node(0)
        dummy.next = self.head
        current = self.head

        while current and current.next:
            print("\n--- New iteration ---")
            print(f"Current node to insert: {current.value}")
            print(
                f"\nChecking current.value = {current.value} <= current.next.value = {current.next.value}"
            )
            if current.value <= current.next.value:
                current = current.next
                print(f"Moving current to {current}")
                continue

            # Need to reposition current.next (toInsert)
            toInsert = current.next
            print(f"Node to insert: {toInsert}")

            current.next = toInsert.next
            print(f"Skipping toInsert, current.next now: {current.next}")

            prev = dummy
            print(
                f"Starting search from dummy to find insertion point for {toInsert}")
            while prev.next.value <= toInsert.value:
                print(f" prev at {prev.next}")
                prev = prev.next

            toInsert.next = prev.next
            prev.next = toInsert
            print(
                f"Inserted {toInsert} after {prev}, toInsert.next now {toInsert.next}")

        self.head = dummy.next

    def printList(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" --> ".join(values))


# Test the list:
li = InsertionSortLinkedList()
li.append(4)
li.append(2)
li.append(5)
li.append(1)
li.append(3)

print("Before sorting")
li.printList()

li.insertion_sort()

print("\nAfter sorting")
li.printList()
