class Node:
    def __init__(self, post_id, content):
        self.id = post_id
        self.content = content
        self.prev = None
        self.next = None


class RecentPostsFeed:
    def __init__(self, max_size=10):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size
        self.map = {}  # post_id -> Node

    def add_post(self, post_id, content):
        if post_id in self.map:
            print(f"Post with ID {post_id} already exists.")
            return

        new_node = Node(post_id, content)
        self.map[post_id] = new_node

        # Add to tail (newest post)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

        # Trim oldest if size exceeds max
        if self.size > self.max_size:
            old_id = self.head.id
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.map.pop(old_id)
            self.size -= 1

    def delete_post(self, post_id):
        if post_id not in self.map:
            print(f"Post {post_id} not found.")
            return

        node = self.map[post_id]

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        del self.map[post_id]
        self.size -= 1

    def edit_post(self, post_id, new_content):
        if post_id in self.map:
            self.map[post_id].content = new_content
        else:
            print(f"Post {post_id} not found.")

    def get_recent_posts(self):
        posts = []
        current = self.head
        while current:
            posts.append(f"{current.id}: {current.content}")
            current = current.next
        return posts


# ==================#

feed = RecentPostsFeed()

# Add some posts
feed.add_post(101, "John's photo at the beach")
feed.add_post(102, "Sarah's blog on remote work")
feed.add_post(103, "Alex's video: Funny cats")

# Edit a post
feed.edit_post(102, "Sarah's updated blog: Remote Work Tips")

# Delete a post
feed.delete_post(103)

# Add more to overflow the limit
for i in range(104, 116):
    feed.add_post(i, f"Post #{i}")

# Show the 10 most recent posts
print("\nRecent Posts Feed:")
for p in feed.get_recent_posts():
    print("•", p)
