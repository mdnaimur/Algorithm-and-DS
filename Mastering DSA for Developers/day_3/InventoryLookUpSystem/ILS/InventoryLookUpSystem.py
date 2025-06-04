from ILS.utils import unique_index
from linked_list.LinkedList import LinkedList


class InventoryLookUpSystem:
    def __init__(self, size=13):
        self.size = unique_index(size)
        self.product_table_db = [None] * self.size
        self.count = 0
        self._keys = set()

    # hash index
    def _hash(self, key):
        hash_value = 7971
        for ch in key:
            hash_value = (hash_value * 33) ^ ord(ch)
       # print("[DeBUG hash]", abs(hash_value) % self.size)
        return abs(hash_value) % self.size

    # TODO resize
    def _resize(self):
        old_product_table = self.product_table_db
        self.size = unique_index(self.size * 2)
        self.product_table_db = [None] * self.size
        self.count = 0

        for products in old_product_table:
            if products:
                for key, value in products.entries():
                    self.product_add(key, value)

    def _insert(self, key, value):
        index = self._hash(key)
        if self.product_table_db[index] is None:
            self.product_table_db[index] = LinkedList()

        new_product = self.product_table_db[index]
        if new_product.find(key) is None:
            self.count += 1
            self._keys.add(key)

        new_product.insert(key, value)

    # product add
    def add(self, key, value):
        if self.count / self.size >= 0.5:
            self._resize()
        self._insert(key, value)

    # product get
    def get(self, key):
        index = self._hash(key)
        get_prodcut = self.product_table_db[index]
        if not get_prodcut:
            return None
        return get_prodcut.find(key)

    # product update
    def update(self, key, new_value):
        index = self._hash(key)
        product_update = self.product_table_db[index]

        if product_update.find(key) is not None:
            product_update._insert(key, new_value)
            return True
        return False

    # product delete
    def delete(self, key):
        index = self._hash(key)
        delete_product = self.product_table_db[index]
        if not delete_product:
            return False

        if delete_product.find(key) is not None:
            delete_product.remove(key)
            self.count -= 1
            self._keys.discard(key)
            return True

        return False

    # all values of product
    def all_values(self):
        products = []
        for items in self.product_table_db:
            if items:
                for _, item in items.entries():  # this entires comes from linkedList
                    products.append(item)
        return products

    # all key
    def all_keys(self):
        return [k for k in self._keys]

    # def get_price(self, key):
    #     product = self.get(key)
    #     return product.price if product else None

    # entries
    def entries(self):
        all_entries = []
        for product in self.product_table_db:
            if product:
                for item in product.entries():
                    all_entries.append(item)

        return all_entries

    # str value
    def __str__(self):
        # this entries() comes from linkedList
        return "\n".join(f" {k}: {v}" for k, v in self.entries())
