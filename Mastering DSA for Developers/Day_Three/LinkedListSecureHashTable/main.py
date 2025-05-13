from hash_table.HashTable import HashTable
import time

# -----------------------------
# Test 1: Basic HashTable Usage
# -----------------------------
print("=== Test 1: Basic Set and Print ===")
hash_table_1 = HashTable()
hash_table_1.set('user', 'naimur')
hash_table_1.set('address', 'Dhaka')
hash_table_1.set('phone', '0172737373', time_set=5)  # Set with TTL
hash_table_1.set('Blood', 'A+')

print("HashTable 1 Contents:\n", hash_table_1)
print("------ End of Test 1 ------\n\n")

# -----------------------------------------
# Test 2: Expiry Check with Time-to-Live (TTL)
# -----------------------------------------
print("=== Test 2: TTL Expiration ===")
hash_table_2 = HashTable()
print("Initial (empty) HashTable 2:", hash_table_2)

hash_table_2.set("user", "techdcsn")
hash_table_2.set("user2", "abc123", time_set=3)  # Will expire after 3 seconds

print("Before TTL Expiry:")
print("  Values:", hash_table_2.values())
print("  Size:", hash_table_2.size)
print("  Bucket Count:", hash_table_2.count)
print("  TTL Info:", hash_table_2.time_set)

# Wait for TTL to expire
time.sleep(3)

print("\nAfter TTL Expiry:")
print("  Get 'user2':", hash_table_2.get("user2"))  # Expected: None
print("  All Items:\n", hash_table_2)
print("------ End of Test 2 ------\n\n")

# -----------------------------------------
# Test 3: Overwriting and Re-checking Expiry
# -----------------------------------------
print("=== Test 3: Reset with TTL and Expiry ===")
hash_table_2.set("user", "naimur")  # Overwrite existing key
# Will expire after 3 seconds
hash_table_2.set("token", "TimeNaimur", time_set=3)

print("Before TTL Expiry:")
print("  Get 'token':", hash_table_2.get("token"))
print("  HashTable Contents:\n", hash_table_2)
print("  Size:", hash_table_2.size)
print("  Bucket Count:", hash_table_2.count)
print("  TTL Info:", hash_table_2.time_set)

# Wait again for TTL to expire
time.sleep(4)

print("\nAfter TTL Expiry:")
print("  Get 'token':", hash_table_2.get("token"))  # Expected: None
print("  Delete key 'token':", hash_table_2.delete("user"))  # Expected: None
print("  Delete key 'token':", hash_table_2.delete("user2"))  # Expected: None
print("  ⭕ All Items:\n", hash_table_2)
print("------ End of Test 3 ------")
