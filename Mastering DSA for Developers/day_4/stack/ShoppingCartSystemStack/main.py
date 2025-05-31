
from stack_product.ProductCart import ProductCart


def print_section(title):
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60 + "\n")


product = ProductCart()

print_section("Add Product Item")
product.addProduct('Dates')
product.addProduct("Apple")
product.addProduct("Orange")
product.addProduct("Mango")

print(product.viewCart())
print_section("View Cart item")
#
products = product.viewCart()
for pro in products:
    print(pro)


print_section("Checkout")
print(product.checkout())
