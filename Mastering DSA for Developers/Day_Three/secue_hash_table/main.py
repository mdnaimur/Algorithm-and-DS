from core.hashtable import SecureHashTable
import time

# -----------------------------------------
# Test 1: Basic Set and TTL Expiry Test
# -----------------------------------------
print("=== Test 1: Set with TTL and Expiry Check ===")

ht = SecureHashTable()
print("Initial (empty) SecureHashTable:", ht)

# Set some keys, including one with TTL
ht.set("user", "techdcsn")
ht.set("user2", "abc123", ttl=3)  # Expires in 3 seconds

# Check values before TTL expiry
print("\nBefore TTL Expiry:")
print("  Values:", ht.values())
print("  Capacity (order):", ht.capacity)
print("  Bucket Count:", ht.buckets)
print("  TTL Store:", ht.ttl_store)

# Wait for TTL to expire
time.sleep(3)

# Check values after TTL expiry
print("\nAfter TTL Expiry:")
print("  Get 'user2':", ht.get("user2"))  # Expected: None
print("  All Items:", ht.items())
print("------ End of Test 1 ------\n\n")

# -----------------------------------------
# Test 2: Overwriting and TTL Expiry Recheck
# -----------------------------------------
print("=== Test 2: TTL Recheck with Overwrite ===")

# Overwrite and set a new key with TTL
ht.set("user", "naimur")
ht.set("token", "tttt", ttl=3)  # Expires in 3 seconds

print("\nBefore TTL Expiry:")
print("  Get 'token':", ht.get("token"))
print("  Full HashTable:\n", ht)
print("  Capacity (order):", ht.capacity)
print("  Bucket Count:", ht.buckets)
print("  TTL Store:", ht.ttl_store)

# Wait for TTL to expire
time.sleep(4)

print("\nAfter TTL Expiry:")
print("  Get 'token':", ht.get("token"))  # Expected: None
print("  All Items:", ht.items())
print("------ End of Test 2 ------")
