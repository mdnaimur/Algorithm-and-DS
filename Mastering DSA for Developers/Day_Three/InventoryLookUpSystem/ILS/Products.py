
class Products:
    def __init__(self, sku,  name, category, price, stock):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dist(self):
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'stock': self.stock
        }

    def __str__(self):
        return f"Product(name = {self.name}, price = {self.price}, stock = { self.stock}, category = {self.category})"
