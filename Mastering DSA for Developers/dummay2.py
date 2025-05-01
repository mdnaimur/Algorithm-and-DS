class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        if not self.head:
            return None

        if self.head.key == key:
            self.head = self.head.next
            return

        current = self.head
        previous = None

        while current and current.key != key:
            previous = current
            current = current.next

        if current:
            previous.next = current.next

        return None

    def entries(self):
        current = self.head
        while current:
            yield (current.key, current.value)
            current = current.next


class HashTable:
    def __init__(self, size=53):
        self.table = [None] * size
        self.size = size
        self.count = 0
        self._keys = set()

    def _hash(self, key):
        hash_val = 5381
        for ch in key:
            hash_val = (hash_val * 33) ^ ord(ch)
        return abs(hash_val) % self.size

    def _resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0
        self._keys = set()

        for bucket in old_table:
            if bucket:
                for key, value in bucket.entries():
                    self.set(key, value)

    def set(self, key, value):
        if self.count / self.size >= 0.5:
            self._resize(self.size * 2)

        index = self._hash(key)
        if not self.table[index]:
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


class HashSet:
    def __init__(self):
        self.data = HashTable()

    def add(self, value):
        val_str = str(value)
        if not self.has(value):
            self.data.set(val_str, True)

    def has(self, value):
        return bool(self.data.get(str(value)))

    def values(self):
        return self.data.keys()


# Example usage and operations
hash_set = HashSet()
hash_set.add(1)
hash_set.add(2)
hash_set.add(3)
hash_set.add(1)

hash_set2 = HashSet()
hash_set2.add(1)
hash_set2.add(2)
hash_set2.add(4)
hash_set2.add(5)
hash_set2.add(6)

hash_set3 = HashSet()
hash_set3.add(1)
hash_set3.add(2)

print("HashSet 1:", hash_set.values())
print("HashSet 2:", hash_set2.values())


def union(setA, setB):
    result = HashSet()
    for value in setA.values():
        result.add(value)
    for value in setB.values():
        result.add(value)
    return result


def intersection(setA, setB):
    result = HashSet()
    for value in setA.values():
        if setB.has(value):
            result.add(value)
    return result


def difference(setA, setB):
    result = HashSet()
    for value in setA.values():
        if not setB.has(value):
            result.add(value)
    return result


def subset(setA, setB):
    for value in setA.values():
        if not setB.has(value):
            return False
    return True


print("Union:", union(hash_set, hash_set2).values())
print("Intersection:", intersection(hash_set, hash_set2).values())
print("Difference:", difference(hash_set, hash_set2).values())
print("Subset:", subset(hash_set3, hash_set))
