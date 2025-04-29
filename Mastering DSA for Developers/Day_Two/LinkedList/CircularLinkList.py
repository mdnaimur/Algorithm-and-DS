class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def remove(self, data):
        if not self.head:
            return False

        current = self.head
        prev = None

        # Case: When head node has the data
        if current.data == data:
            if self.size == 1:
                self.head = None
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = self.head.next
                last.next = self.head
            self.size -= 1
            return True

        # Search in other nodes for remove
        while True:
            prev = current
           # print("[DUBUG]: prev value checkd 🙋‍♂️ ", prev.data)
            current = current.next
            print("[DUBUG]: current  value checkd 👉 ", current.data)
            print("[self.head]: checked: ❗  ", self.head.data)
            if current.data == data:
                prev.next = current.next
                self.size -= 1
                return True
            if current == self.head:
                break

        return False

    def to_list(self):
        if not self.head:
            return "Empty List"

        result = []
        current = self.head
        while True:
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        return " --> ".join(result) + " --> (head)"

    def __str__(self):
        if not self.head:
            return "Empty List"

        result = []
        current = self.head
        while True:
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        return " --> ".join(result) + " --> (head)"


circularList = CircularLinkList()
circularList.insert(40)
circularList.insert(50)
circularList.insert(60)
circularList.insert(70)
circularList.insert(80)

print("circular link list", circularList)
circularList.remove(70)
print("after circular link list remove ❌ data ", circularList)
