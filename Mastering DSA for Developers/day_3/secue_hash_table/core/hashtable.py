import time
from core.utils import next_prime


class SecureHashTable:
    def __init__(self, initial_capacity=7, load_factor=0.75):
        self.capacity = next_prime(initial_capacity)
        print("Capcicty check", self.capacity)
        self.size = 0
        self.load_factor = load_factor
        self.buckets = [[] for _ in range(self.capacity)]
        print("Chekcing bucket: ", self.buckets)
        self.key_order = []
        self.ttl_store = {}

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_buckets = self.buckets
        self.capacity = next_prime(self.capacity * 2)
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for k, v in bucket:
                if not self._is_expired(k):
                    self._insert(k, v, resize=False)

    def _is_expired(self, key):
        ttl = self.ttl_store.get(key)
        if ttl and ttl < time.time():
            self.delete(key)
            return True
        return False

    def _insert(self, key, value, ttl=None, resize=True):
        if resize and self.size / self.capacity > self.load_factor:
            self._resize()
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print(f"inside insert check bucket[{i}] = ({key}, {value})")
                return

        bucket.append((key, value))
        self.size += 1
        if key not in self.key_order:
            self.key_order.append(key)
        if ttl:
            self.ttl_store[key] = time.time() + ttl

    def set(self, key, value, ttl=None):
        self._insert(key, value, ttl=ttl)

    def get(self, key):
        if self._is_expired(key):
            return None

        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        self.key_order = [k for k in self.key_order if k != key]
        self.ttl_store.pop(key, None)

    def keys(self):
        return [k for k in self.key_order if not self._is_expired(k)]

    def values(self):
        return [self.get(k) for k in self.keys()]

    def items(self):
        return [(k, self.get(k)) for k in self.keys()]

    def __len__(self):
        return len(self.keys())

    def __str__(self):
        return str(dict(self.items()))
