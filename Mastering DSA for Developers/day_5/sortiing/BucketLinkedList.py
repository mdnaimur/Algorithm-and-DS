class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SortLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


def bucketSortWithLinkedList(arr):
    n = len(arr)
    if n <= 0:
        return arr
    print(f"Orginal arrya: {arr}")
    buckets = [SortLinkedList() for _ in range(n)]
    print(f"Initialized {n} sorted linked list buckets.")

    for i in range(n):
        index = int(arr[i] * n)
        print(f"Inserting {arr[i]} into bucket index {index}")
        buckets[index].insert(arr[i])

    result = []
    for i, bucket in enumerate(buckets):
        bucket_list = bucket.to_list()
        print(f"Bucket {i} contents:{bucket_list}")
        result.extend(bucket_list)

    print(f"Sorted result:{result}")
    return result


arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorted_arr_with_linked_list = bucketSortWithLinkedList(arr)
