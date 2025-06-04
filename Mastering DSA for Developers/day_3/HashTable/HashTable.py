class HashTable:
    def __init__(self):
        self.table = [None] * 100  # fixed size array

    def _hash(self, key):
        hash_value = 999
        for char in key:
            hash_value += ord(char)
        return hash_value % len(self.table)

    def set(self, key, value):
        index = self._hash(key)
        print("[⭕] set index after hash:", index)
        self.table[index] = value

    def get(self, key):
        index = self._hash(key)
        print("[⭕] get the index:", index)
        return self.table[index]

    def remove(self, key):
        index = self._hash(key)
        self.table[index] = None


hash_table = HashTable()
hash_table.set('name', 'Md Naimur Rahman')
hash_table.set("age", 29)


print("Get Hashvalue: ", hash_table.get('age'))
print("Get Hashvalue: ", hash_table.get('name'))

hash_table.remove('name')

print("after remove Hashvalue: ", hash_table.get('name'))
