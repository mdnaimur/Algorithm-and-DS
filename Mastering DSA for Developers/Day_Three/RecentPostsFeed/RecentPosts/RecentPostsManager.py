from DoubleLinkList.DoubleLinkedList import DoubleLinkedList


class RecentPostsManager:
    def __init__(self, max_size=10):
        self.size = 0
        self.posts = DoubleLinkedList()
        self.count = 0

    def add_post(self, post):
        pass
