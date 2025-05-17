from ILS.Products import Products
from ILS.InventoryLookUpSystem import InventoryLookUpSystem


class InventoryManager:
    def __init__(self):
        self.database = InventoryLookUpSystem()

    def add_product(self, product):
        self.database.add(product.sku, product)

    def update_stock(self, sku, stock):
        product = self.database.get(sku)
        if product:
            product.stock = str(stock)
            return True
        return False

    def delete_product(self, sku):
        return self.database.delete(sku)

    def get_product(self, sku):
        return self.database.get(sku)

    def get_price(self, sku):
        product = self.database.get(sku)
        if product:
            return product.price
        return None

    def get_name(self, sku):
        product = self.database.get(sku)
        if product:
            return product.name
        return None

    def get_category(self, sku):
        product = self.database.get(sku)
        if product:
            return product.category
        return None

    def get_stock(self, sku):
        product = self.database.get(sku)
        if product:
            return product.stock
        return None

    def all_keys(self):
        return self.database.all_keys()

    def all_values(self):
        return self.database.all_values()
