class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedLst:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def remove(self, data):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.data != data:
                current = current.next
                continue

            if current == self.head and current == self.tail:
                self.head = None
                self.tail = None
                self.size -= 1
                return True

            if current == self.head:
                self.head = current.next
                if self.head:
                    self.head.prev = None
                self.size -= 1
                return True

            if current == self.tail:
                self.tail = current.prev
                if self.tail:
                    self.tail.next = None
                self.size -= 1
                return True

            print("$ Current value", current.data)
            print("$ [Current.next ⭕] value", current.next.data)
            print("$ [Current.prev 🙋‍♂️] value", current.prev.data)
            current.prev.next = current.next
            print("[DEBUG:🚑] (current.prev.next)", current.prev.next.data)
            current.next.prev = current.prev
            print("[DEBUG:🚑] (current.next.prev)", current.next.prev.data)
            self.size -= 1
            return True

        return False

    def __str__(self):
        if not self.head:
            return "Empty List"

        array = []
        current = self.head
        while current:
            array.append(str(current.data))
            current = current.next
        return " <--> ".join(array) + " <--> [null]"


doubleLinkList = DoubleLinkedLst()

doubleLinkList.append(30)
doubleLinkList.append(40)
doubleLinkList.append(50)
doubleLinkList.append(60)
doubleLinkList.append(70)

print("Double linklist value: ", doubleLinkList)
doubleLinkList.remove(50)
print("Afater Remove", doubleLinkList)
