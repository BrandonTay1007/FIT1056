class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.comments = []

class comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author

class forum:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_posts(self):
        return self.posts

