# hash_table/HashTable.py


class HashTable:
    def __init__(self, size=53):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.count = 0

    def _hash(self, key, i=0):
        hash_val = 0
        prime = 31
        for char in str(key):
            hash_val = (hash_val * prime + ord(char)) % self.size
        return (hash_val + i) % self.size

    def _probe(self, key):
        for i in range(self.size):
            idx = self._hash(key, i)
            if self.keys[idx] is None or self.keys[idx] == key:
                return idx
        raise Exception("HashTable is full")

    def set(self, key, value):
        idx = self._probe(key)
        if self.keys[idx] is None:
            self.count += 1
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        for i in range(self.size):
            idx = self._hash(key, i)
            if self.keys[idx] is None:
                return None
            if self.keys[idx] == key:
                return self.values[idx]
        return None

    def delete(self, key):
        for i in range(self.size):
            idx = self._hash(key, i)
            if self.keys[idx] == key:
                self.keys[idx] = None
                self.values[idx] = None
                self.count -= 1
                return True
            if self.keys[idx] is None:
                break
        return False

    def all_values(self):
        return [val for val in self.values if val is not None]

    def all_keys(self):
        return [key for key in self.keys if key is not None]

    def entries(self):
        return [(self.keys[i], self.values[i]) for i in range(self.size) if self.keys[i] is not None]

    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.entries())


# models/product.py

class Product:
    def __init__(self, sku, name, quantity, price):
        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.sku}: {self.name} ({self.quantity} in stock @ ${self.price})"

    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }


# inventory/manager.py


class InventoryManager:
    def __init__(self):
        self.table = HashTable()

    def add_product(self, product):
        self.table.set(product.sku, product)

    def update_stock(self, sku, quantity):
        product = self.table.get(sku)
        if product:
            product.quantity = quantity
            return True
        return False

    def delete_product(self, sku):
        return self.table.delete(sku)

    def get_product(self, sku):
        return self.table.get(sku)

    def list_products(self):
        return self.table.all_values()

    def low_stock(self, threshold=5):
        return [p for p in self.table.all_values() if p.quantity <= threshold]


# main.py


manager = InventoryManager()

# Add some products
manager.add_product(Product("P100", "Tablet", 15, 200.00))
manager.add_product(Product("X999", "Speaker", 3, 80.00))
manager.add_product(Product("M450", "Mouse", 2, 25.00))

# List all
print("=== Inventory ===")
for item in manager.list_products():
    print(item)

# Check low stock
print("\n=== Low Stock Items ===")
for item in manager.low_stock():
    print(item)

# Update stock
manager.update_stock("M450", 10)

# Delete a product
manager.delete_product("X999")

# Final Inventory
print("\n=== Final Inventory ===")
for item in manager.list_products():
    print(item)
