import time
from core.hashtable import SecureHashTable


def test_ttl_expiry():
    ht = SecureHashTable()
    ht.set("a", "1", ttl=1)
    time.sleep(2)
    assert ht.get("a") is None


def test_order_preservation():
    ht = SecureHashTable()
    ht.set("a", "1")
    ht.set("b", "2")
    ht.set("c", "3")
    assert ht.keys() == ["a", "b", "c"]


def test_resize():
    ht = SecureHashTable(initial_capacity=3)
    for i in range(10):
        ht.set(f"key{i}", f"value{i}")
    assert len(ht) == 11
