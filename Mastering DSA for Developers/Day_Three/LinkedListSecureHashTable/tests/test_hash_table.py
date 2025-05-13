import unittest
import time
from hash_table.HashTable import HashTable


class TestHashTable(unittest.TestCase):

    def test_set_and_get(self):
        ht = HashTable()
        ht.set('name', 'naimur')
        self.assertEqual(ht.get('name'), 'naimur')

    def test_overwrite_value(self):
        ht = HashTable()
        ht.set('name', 'naimur')
        ht.set('name', 'rahman')
        self.assertEqual(ht.get('name'), 'rahman')

    def test_get_nonexistent_key(self):
        ht = HashTable()
        self.assertIsNone(ht.get('nonexistent'))

    def test_delete_existing_key(self):
        ht = HashTable()
        ht.set('name', 'naimur')
        result = ht.delete('name')
        self.assertTrue(result)
        self.assertIsNone(ht.get('name'))

    def test_delete_nonexistent_key(self):
        ht = HashTable()
        result = ht.delete('ghost')
        self.assertFalse(result)

    def test_keys_method(self):
        ht = HashTable()
        ht.set('a', 1)
        ht.set('b', 2)
        keys = ht.keys()
        self.assertIn('a', keys)
        self.assertIn('b', keys)
        self.assertEqual(len(keys), 2)

    def test_values_method(self):
        ht = HashTable()
        ht.set('x', 10)
        ht.set('y', 20)
        values = ht.values()
        self.assertIn(10, values)
        self.assertIn(20, values)
        self.assertEqual(len(values), 2)

    def test_entries_method(self):
        ht = HashTable()
        ht.set('k1', 'v1')
        ht.set('k2', 'v2')
        entries = ht.entries()
        self.assertIn(('k1', 'v1'), entries)
        self.assertIn(('k2', 'v2'), entries)

    def test_str_method(self):
        ht = HashTable()
        ht.set('user', 'naimur')
        result = str(ht)
        self.assertIn('user: naimur', result)

    def test_ttl_expiration(self):
        ht = HashTable()
        ht.set('session', 'abc123', time_set=2)
        self.assertEqual(ht.get('session'), 'abc123')
        time.sleep(3)
        self.assertIsNone(ht.get('session'))

    def test_resize_on_threshold(self):
        ht = HashTable(size=5)
        for i in range(10):  # trigger resize
            ht.set(f'key{i}', i)
        self.assertGreaterEqual(ht.size, 10)
        self.assertEqual(ht.get('key5'), 5)

    def test_set_with_same_key_does_not_increase_count(self):
        ht = HashTable()
        ht.set('dup', 'first')
        count_before = ht.count
        ht.set('dup', 'second')  # overwrite
        count_after = ht.count
        self.assertEqual(count_before, count_after)
        self.assertEqual(ht.get('dup'), 'second')

    def test_set_with_ttl_overwrites(self):
        ht = HashTable()
        ht.set('token', 'abc', time_set=2)
        time.sleep(1)
        ht.set('token', 'xyz', time_set=2)  # overwrite with new TTL
        time.sleep(1.5)
        self.assertEqual(ht.get('token'), 'xyz')


if __name__ == '__main__':
    unittest.main()
