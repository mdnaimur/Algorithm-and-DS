
from stack_product.Node import Node


class ProductCart:
    def __init__(self, max_size=10):
        self.display_stack = None
        self.checkout_stack = None
        self.__maxSize = max_size
        self.__d_size = 0

    def addProduct(self, product):
        if self._isFull():
            raise Exception(
                "Cart Item Full! Purchase or remove cart product first")

        newProduct = Node(product)
        newProduct.next = self.display_stack
        self.display_stack = newProduct
        self.__d_size += 1

    def popProduct(self):
        if self._isEmpty():
            raise Exception("No item in this cart...")

        data = self.display_stack.data
        self.display_stack = self.display_stack.next
        self.__d_size -= 1
        return data

    def viewCart(self):
        current = self.display_stack
        buckets = []
        while current:
            buckets.append(current.data)
            current = current.next
        return buckets

    def checkout(self):
        while self.display_stack:
            newItem = self.popProduct()
            new_node_checkout = Node(newItem)
            new_node_checkout.next = self.checkout_stack
            self.checkout_stack = new_node_checkout

        print("Processing checkout (Oldest to Newest):\n")
        while self.checkout_stack:
            print(self.checkout_stack.data)
            self.checkout_stack = self.checkout_stack.next

    def clear(self):
        # self.checkout_stack = None
        self.display_stack = None
        self.__d_size = 0

    def _isEmpty(self):
        return self.__d_size == 0

    def _isFull(self):
        return self.__maxSize <= self.__d_size

    def getSize(self):
        return self.__d_size

    def __str__(self):
        current = self.display_stack
        buckets = []
        count = 1
        while current:
            buckets .append(f"{count}. {current.data}")
            current = current.next
            count += 1

        # return f"Products ({i}): {buckets}"
        return "\n".join(buckets)
