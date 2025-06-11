class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
        dummy = Node(0)
        current = self.head

        while current:
            print("\n--- New iteration ---")
            print(f"Current node to insert: {current.value}")

            prev = dummy
            next_node = current.next  # Save the next node to process later
            print(
                f"Next node saved: {next_node.value if next_node else 'None'}")

            # Find the correct position to insert current
            while prev.next and prev.next.value < current.value:
                print(
                    f"Looking for insert position: {prev.next.value} < {current.value}, moving prev forward")
                prev = prev.next

            print(
                f"Inserting {current.value} after node with value: {prev.value if prev != dummy else 'Dummy'}")

            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            # Show current state of sorted list
            sorted_part = []
            node = dummy.next
            while node:
                sorted_part.append(str(node.value))
                node = node.next
            print("Sorted part now:", " --> ".join(sorted_part))

            # Move to next node
            current = next_node

        self.head = dummy.next  # Update head to point to new sorted list
        print("\n=== Sorting complete ===")
    # Update head to the new sorted list

    def printList(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(" --> ".join(values))


li = InsertionSortLinkedList()
li.append(4)
li.append(2)
li.append(5)
li.append(1)
li.append(3)

print("Before sorting")
li.printList()
li.insertion_sort()
print("After sorting")
li.printList()


'''
 def insertion_sort(self):
        dummy = Node(0)
        current = self.head

        while current:
            prev = dummy
            next_node = current.next

            # Find where to insert current node
            while prev.next and prev.next.value < current.value:
                prev = prev.next

            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current

            current = next_node

        self.head = dummy.next  # Update head to the new sorted list


'''
