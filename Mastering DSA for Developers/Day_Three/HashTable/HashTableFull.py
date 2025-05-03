class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        existing_node = self._find_node(key)
        if existing_node:
            existing_node.value = value
            return

        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def _find_node(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def find(self, key):
        node = self._find_node(key)
        return node.value if node else None

    def entries(self):
        current = self.head
        while current:
            yield (current.key, current.value)
            current = current.next


class HashTable:
    def __init__(self, size=3):
        self.size = size
        self.table = [None] * size
        self._keys = set()
        self.count = 0

    def _hash(self, key, size=None):
        if size is None:
            size = self.size

        has_value = 5381
        for ch in key:
            has_value = (has_value * 33) ^ ord(ch)
        return abs(has_value) % size

    def _resize(self, new_size):
        pass

    def set(self, key, value):

        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = LinkedList()

        bucket = self.table[index]
        if bucket.find(key) is None:
            self.count += 1
            self._keys.add(key)

        bucket.insert(key, value)

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if not bucket:
            return None
        return bucket.find(key)

    def keys(self):
        return list(self._keys)

    def values(self):
        values = []
        for bucket in self.table:
            if bucket:
                for _, value in bucket.entries():
                    values.append(value)

        return values

    def entries(self):
        all_entries = []
        for bucket in self.table:
            if bucket:
                for entry in bucket.entries():
                    all_entries.append(entry)

        return all_entries


hash_table = HashTable()

hash_table.set("name", "Md Naimur Rahman")
hash_table.set("phone", "01521438923")
hash_table.set("city", "Dhaka")
print(hash_table.entries())
print(hash_table.keys())
print(hash_table.values())
print(hash_table.get("name"))
