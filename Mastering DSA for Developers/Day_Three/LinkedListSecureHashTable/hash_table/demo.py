class HashTable:
    def __init__(self, size=53):
        self.table = [None] * size
        self.size = size
        self.count = 0

    def _hash(self, key):
        hash_value = 0
        prime = 31
        for i, char in enumerate(key):
            hash_value = (hash_value * prime + ord(char)) % self.size
        return hash_value

    def set(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket is None:
            return None
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if bucket is None:
            return
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return

    def list_items(self):
        for index, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {index}: {bucket}")

    # Custom functions to retrieve individual attributes
    def get_product_name(self, key):
        product = self.get(key)
        if product:
            return product.get("name", None)
        return None

    def get_product_price(self, key):
        product = self.get(key)
        if product:
            return product.get("price", None)
        return None

    def get_product_quantity(self, key):
        product = self.get(key)
        if product:
            return product.get("quantity", None)
        return None

    def search(self, field, value):
        """Search items where a specific field (e.g., name) matches a value."""
        results = []
        for bucket in self.table:
            if bucket:
                for k, v in bucket:
                    if isinstance(v, dict) and v.get(field) == value:
                        results.append((k, v))
        return results


ht = HashTable()

# Inserting sample products
ht.set("P001", {"name": "Laptop", "quantity": 10, "price": 999.99})
ht.set("P002", {"name": "Mouse", "quantity": 50, "price": 25.00})
ht.set("P003", {"name": "Keyboard", "quantity": 30, "price": 45.00})

# Get product name for P001
print(ht.get_product_name("P001"))  # Output: Laptop

# Get product price for P002
print(ht.get_product_price("P002"))  # Output: 25.00

# Get product quantity for P003
print(ht.get_product_quantity("P003"))  # Output: 30

# If the product doesn't exist
print(ht.get_product_name("P005"))  # Output: None (since P005 doesn't exist)


matches = ht.search("name", "Laptop")
print("Search results for name = 'Laptop':")
for item in matches:
    print(item)
