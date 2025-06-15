class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head or value < self.head.val:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.val < value:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


class BucketSorter:
    def __init__(self, num_buckets=None):
        self.num_buckets = num_buckets

    def sort(self, arr):
        n = len(arr)
        if n <= 0:
            print("Empty array.")
            return arr

        bucket_count = self.num_buckets if self.num_buckets else n
        print(f"Original array: {arr}")
        print(f"Using {bucket_count} buckets.")

        # Create empty sorted linked list buckets
        buckets = [SortedLinkedList() for _ in range(bucket_count)]

        # Distribute input array into buckets
        for val in arr:
            index = int(val * bucket_count)
            print(f"Inserting {val} into bucket index {index}")
            buckets[index].insert(val)

        # Collect results
        result = []
        for i, bucket in enumerate(buckets):
            bucket_list = bucket.to_list()
            print(f"Bucket {i} contents: {bucket_list}")
            result.extend(bucket_list)

        print(f"Sorted result: {result}")
        return result


arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorter = BucketSorter()
sorted_arr = sorter.sort(arr)
