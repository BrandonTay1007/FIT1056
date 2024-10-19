class forum:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_posts(self):
        return self.posts

    def init_posts(self):
        post_data = extract_file_info(FORUM_FILE_PATH)
        for post in post_data:
            self.posts.append(post)

