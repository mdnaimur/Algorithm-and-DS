from linked_list.LinkedList import LinkedList
import time
from hash_table.utiles import next_prime


class HashTable:
    def __init__(self, size=53):
        self.size = next_prime(size)
        self.table = [None] * size
        self.count = 0
        self.time_set = {}
        self._keys = set()

    def _hash(self, key):
        hash_value = 7899
        for ch in key:
            hash_value = (hash_value * 33) ^ ord(ch)

        return abs(hash_value) % self.size

    def _resize(self):
        old_table = self.table
        self.size = next_prime(self.size * 2)
        self.table = [None] * self.size
        self.count = 0

        for bucket in old_table:
            if bucket:
                for key, value in bucket.entries():
                    if not self._is_expired:
                        self.set(key, value)

    def _is_expired(self, key):
        timeOut = self.time_set.get(key)
        if timeOut and timeOut < time.time():
            self.delete(key)
            return True
        return False

    def _insert(self, key, value, time_set=None):
        index = self._hash(key)
        self.table[index] = LinkedList()

        bucket = self.table[index]
        if bucket.find(key) is None:
            self.count += 1
            self._keys.add(key)

        bucket.insert(key, value)

        if time_set:
            self.time_set[key] = time.time() + time_set

    def set(self, key, value, time_set=None):
        if self.count / self.size >= 0.5:
            self._resize()

        self._insert(key, value, time_set=time_set)

    def get(self, key):
        # expired key
        if self._is_expired(key):
            return None

        index = self._hash(key)
        bucket = self.table[index]
        # print("I am inside bucket", bucket)
        if not bucket:
            return None
        return bucket.find(key)

    def keys(self):
        return [k for k in self._keys if not self._is_expired(k)]

    def values(self):
        values = []
        for bucket in self.table:
            if bucket:
                for _, value in bucket.entries():
                    values.append(value)

        return values

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if not bucket:
            return False

        if bucket.find(key) is not None:
            bucket.remove(key)
            self._keys.discard(key)  # delete the crospoding key
            self.count -= 1
            self.time_set.pop(key, None)  # time set remove
            return True

        return False

    def entries(self):
        all_entries = []
        for bucket in self.table:
            if bucket:
                for entry in bucket.entries():
                    all_entries.append(entry)
        return all_entries

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.entries())


# hastbl = HashTable()
# hastbl.set('user', 'naimur')
# print(hastbl)
