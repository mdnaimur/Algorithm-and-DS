
from ILS.InventoryManager import InventoryManager
from ILS.Products import Products
from ILS.InventoryLookUpSystem import InventoryLookUpSystem

# Get the absolute path of the current file (main.py)
# current_file_path = os.path.abspath(__file__)
# project_root = os.path.dirname(current_file_path)

# # Add the root directory to sys.path
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)

# Now import your modules


def print_section(title):
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60 + "\n")


product = Products('p90', 'BCS book', 'Stationary', '1505', '10')
# print(product.to_dist())

ils = InventoryLookUpSystem()

ils.add('p90', product)

print("Product list", ils)
# print_section('Obj type')
# print("Obj list", ils)
# print_section('allProduct')
# print("all Product", ils.all_values())
# print_section('product get')
# print("Product list", ils.get('p10'))
# print("Product list", ils)
# print_section('..')

# Create Inventory


# Add Product
product1 = Products('p10', 'Pen', 'Stationary', '100', '10')
ils.add('p10', product1)

product2 = Products('p20', 'Notebook', 'Stationary', '250', '15')
ils.add('p20', product2)

# View all products
print_section("All Products")
print(ils)

# Search and print price
# print_section("Search Product Price")
# price = ils.get_price('p90')
# if price:
#     print(f"Price of p90: {price}")
# else:
#     print("Product not found.")


print_section("Inventory Manager")

manager = InventoryManager()

# Test 1: Add products
print_section("Test 1: Add Products")
prod1 = Products('p10', 'Pen', 'Stationary', '100', '10')
prod2 = Products('p20', 'Notebook', 'Stationary', '250', '15')
prod3 = Products('p30', 'Backpack', 'Bags', '800', '5')

manager.add_product(prod1)
manager.add_product(prod2)
manager.add_product(prod3)

print(manager.all_keys())
print_section("All values")
values = manager.all_values()
for value in values:
    print("VALUEs ", value)


print("Added products:")
for sku in manager.all_keys():
    print(manager.get_product(sku))

# Test 2: Get price
print_section("Test 2: Get Product Price")
print("Price of p10:", manager.get_price('p10'))
print("Price of p20:", manager.get_price('p20'))
print("Price of p30:", manager.get_price('p30'))
print("Price of p30:", manager.get_price('p330'))

# Test 2.2: Get name
print_section(" Get Product name")
print("name of p10:", manager.get_name('p10'))
print("name of p20:", manager.get_name('p20'))
print("name of p30:", manager.get_name('p30'))

# Test 2.3: Get category
print_section("category  2: Get Product category")
print("category of p10:", manager.get_category('p10'))
print("category of p20:", manager.get_category('p20'))
print("Price of p30:", manager.get_category('p30'))

# Test 2.4: Get stock
print_section("Stock  : Get Product stock")
print("stock of p10:", manager.get_stock('p10'))
print("stock of p20:", manager.get_stock('p20'))
print("stock of p30:", manager.get_stock('p30'))

# Test 3: Update stock
print_section("Test 3: Update Stock")
print("Before update:", manager.get_product('p30').stock)
manager.update_stock('p30', 12)
print("After update:", manager.get_product('p30').stock)

# Test 4: Delete a product
print_section("Test 4: Delete Product")
deleted = manager.delete_product('p20')
print("Deleted p20:", deleted)
print("Trying to get p20:", manager.get_product('p20'))

# Test 5: Handle non-existent SKU
print_section("Test 5: Non-existent SKU Operations")
print("Get price of p999:", manager.get_price('p999'))
print("Update stock of p999:", manager.update_stock('p999', 50))
print("Delete p999:", manager.delete_product('p999'))

# Test 6: Add duplicate product SKU (should overwrite)
print_section("Test 6: Add Duplicate SKU (Overwrite)")
prod1_updated = Products('p10', 'Pen Pro', 'Stationary', '150', '25')
manager.add_product(prod1_updated)
print("Updated p10:", manager.get_product('p10'))
print("New Price of p10:", manager.get_price('p10'))
