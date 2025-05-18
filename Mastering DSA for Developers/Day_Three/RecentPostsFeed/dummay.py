class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, max_size=10):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1
        if self.size > self.max_size:
            self.pop_front()

    def pop_front(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result


class RecentPostsFeed:
    def __init__(self):
        self.posts = DoublyLinkedList(max_size=10)

    def add_post(self, post):
        self.posts.append(post)

    def get_recent_posts(self):
        return self.posts.to_list()

    def show_feed(self):
        print("Recent Posts (Oldest → Newest):")
        for post in self.get_recent_posts():
            print("-", post)
