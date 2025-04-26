class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkList:
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
        self.head = new_node

    def insert_at(self, data, position):
        if position < 0 or position > self.size:
            return False

        if position == 0:
            self.prepend(data)
            return True

        if position == self.size:
            self.append(data)
            return True

        new_node = Node(data)
        current = self.head
        previous = None
        index = 0
        while index < position:
            previous = current
            current = current.next
            index += 1

        new_node.next = current
        previous.next = new_node
        return True

    def get(self, position):
        if position < 0 or position >= self.size:
            return None
        current = self.head
        index = 0

        while index < position:
            current = current.next
            index += 1

        return current.data

    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def get_size(self):
        return self.size

    def remove(self, data):
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return True

        current = self.head

        while current.next:
            if current.next.data == data:
                print(f"[DEBUG] inside remove : {current.next.data}")
                current.next = current.next.next
                print(
                    f"[DEBUG] inside remove current.next.next : {current.next.data}")
                self.size -= 1
                if not current.next:
                    self.tail = current
                return True
            current = current.next
        return False

    def remove_at(self, position):
        if position < 0 or position >= self.size:
            raise IndexError("Invalid Index Postion")

        if position == 0:
            removed_node = self.head
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            current = self.head
            previous = None
            index = 0
            while index < position:
                previous = current
                current = current.next
                index += 1
            removed_node = current
            previous.next = current.next
            if not current.next:
                self.tail = previous
        self.size -= 1
        return removed_node.data

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def to_array(self):
        element = []
        current = self.head
        while current:
            element.append(current.data)
            current = current.next
        return element

    def __str__(self):
        element_array = []
        current = self.head
        while current:
            element_array.append(str(current.data))
            current = current.next
        return " -> ".join(element_array) + " -> None"


link = SingleLinkList()

link.append(59)
link.append(99)
link.append(39)
link.append(79)

print("After appending ", link.to_array())
# link.remove(39)
link.remove_at(2)
print("After remove ", link.to_array())
link.prepend(100)
print("After Prepned ", link)
print("After Prepned size ", link.size)
link.insert_at(157, 4)
print("After isertAt: ", link)
print("After isertAt size: ", link.size)

get_data = link.get(4)
print("After getting data: ", get_data)
if link.contains(99):
    print("Data found")
else:
    print("not found")

linkData = link
print("copy data get size", linkData.to_array())

print("After Data clean: ", link.clear())

if link.is_empty():
    print("Value is empthy after clear")
else:
    print("Value found")


print("copy data get size", linkData.get_size())
