from DoubleLinkList.DoubleLinkedList import DoubleLinkedList


class RecentPostsManager:
    def __init__(self, max_size=10):
        self.size = 0
        self.posts = DoubleLinkedList()
        self.maxsize = max_size

    def add_post(self, post):
        '''
        if add size > maxSize 
        then preRemove 
        '''
        self.posts.append(post)
        self.size += 1
        # print("[DEBUG= size]", self.size)
        if self.size > self.maxsize:
            self.posts.pop_front()
            self.size -= 1

    def get_recent_post(self):
        posts = self.posts.to_list()[::-1]
        # resutl = ""
        resutl = {}
        for i, post in enumerate(posts):
            # resutl += f"{i}.{post}\n"
            resutl[i] = post
        return resutl
