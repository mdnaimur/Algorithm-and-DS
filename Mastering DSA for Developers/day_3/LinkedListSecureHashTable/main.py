from hash_table.HashTable import HashTable
import time

# Utility for section formatting


def print_section(title):
    print("\n" + "=" * 60)
    print(f"{title}")
    print("=" * 60 + "\n")


# ---------------------------------------------------
# Test 1: Basic Set and Get
# ---------------------------------------------------
print_section("Test 1: Basic `set()` and `get()`")
ht1 = HashTable()
ht1.set("name", "Naimur")
ht1.set("city", "Dhaka")

print("Get 'name':", ht1.get("name"))        # Expected: Naimur
print("Get 'city':", ht1.get("city"))        # Expected: Dhaka
print("Get 'country':", ht1.get("country"))  # Expected: None

# ---------------------------------------------------
# Test 2: Delete Operation
# ---------------------------------------------------
print_section("Test 2: `delete()` Key")
ht1.set("email", "test@example.com")
print("Before delete - email:", ht1.get("email"))
print("Delete result:", ht1.delete("email"))  # Expected: True
print("After delete - email:", ht1.get("email"))  # Expected: None

# ---------------------------------------------------
# Test 3: TTL Expiry Handling
# ---------------------------------------------------
print_section("Test 3: Time-To-Live (TTL) Expiry")
ht2 = HashTable()
ht2.set("session", "abc123", time_set=2)
print("Immediately after set:", ht2.get("session"))  # Expected: abc123
time.sleep(3)
print("After 3 seconds (expired):", ht2.get("session"))  # Expected: None

# ---------------------------------------------------
# Test 4: Overwriting Values
# ---------------------------------------------------
print_section("Test 4: Overwriting Existing Key")
ht2.set("user", "old_user")
print("Before overwrite:", ht2.get("user"))
ht2.set("user", "new_user")
print("After overwrite:", ht2.get("user"))  # Expected: new_user

# ---------------------------------------------------
# Test 5: Keys, Values, Entries
# ---------------------------------------------------
print_section("Test 5: `keys()`, `values()`, and `entries()`")
ht3 = HashTable()
ht3.set("product", "Laptop")
ht3.set("price", "$1000")
ht3.set("brand", "Lenovo")

print("Keys:", ht3.keys())         # ['product', 'price', 'brand']
print("Values:", ht3.values())     # ['Laptop', '$1000', 'Lenovo']
print("Entries:", ht3.entries())   # [('product', 'Laptop'), ...]

# ---------------------------------------------------
# Test 6: String Representation
# ---------------------------------------------------
print_section("Test 6: `__str__()` Representation")
print(ht3)

# ---------------------------------------------------
# Test 7: Resize Trigger on Threshold
# ---------------------------------------------------
print_section("Test 7: Automatic Resize on Load Factor")
ht4 = HashTable(size=5)  # Force small initial size
for i in range(10):
    ht4.set(f"key{i}", f"value{i}")
print("Final size after resize:", ht4.size)   # Expected: Increased
print("Keys:", ht4.keys())                    # Expect all 10 keys

# ---------------------------------------------------
# Test 8: TTL Overwrite and Reset
# ---------------------------------------------------
print_section("Test 8: TTL Reset After Overwrite")
ht5 = HashTable()
ht5.set("token", "temp1", time_set=2)
time.sleep(1)
ht5.set("token", "temp2", time_set=3)  # Extend TTL
time.sleep(2)
print("Get 'token' after 3s (should still exist):", ht5.get("token"))
time.sleep(2)
print("Get 'token' after 5s (should be expired):", ht5.get("token"))

# ---------------------------------------------------
# Test 9: Multiple TTL Keys
# ---------------------------------------------------
print_section("Test 9: Multiple Keys with Different TTLs")
ht6 = HashTable()
ht6.set("short_lived", "1s", time_set=1)
ht6.set("long_lived", "5s", time_set=5)
time.sleep(2)
print("short_lived (should be None):", ht6.get("short_lived"))
print("long_lived (should still exist):", ht6.get("long_lived"))

# ---------------------------------------------------
# Test 10: Non-existent Delete and Get
# ---------------------------------------------------
print_section("Test 10: Get and Delete Non-Existent Keys")
ht7 = HashTable()
print("Get 'missing':", ht7.get("missing"))        # Expected: None
print("Delete 'missing':", ht7.delete("missing"))  # Expected: False
