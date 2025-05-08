from core.hashtable import SecureHashTable
import time

ht = SecureHashTable()

ht.set("user", "techdcsn")
ht.set("token", "abc123", ttl=3)

print("Initial:", ht.get("token"))  # ➜ "abc123"
time.sleep(3)
print("After TTL:", ht.get("token"))  # None
print("All items:", ht.items())


ht.set("user", "naimur")
ht.set("token", "tttt", ttl=3)

print("Initial:", ht.get("token"))  # ➜ "abc123"
time.sleep(4)
print("After TTL:", ht.get("token"))  # None
print("All items:", ht.items())
