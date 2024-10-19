import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_management import *
from app.empoweru_constants import *
from app.posts import Post  

class Forum:
    def __init__(self):
        self.posts = []
        self.init_posts()
        print(len(self.posts))
    def add_post(self, post):
        self.posts.append(post)

    def get_posts(self):
        return self.posts

    def init_posts(self):
        print("\033[92mInitializing posts\033[0m")
        post_data = extract_file_info(FORUM_FILE_PATH)
        for post in post_data:
            post_obj = Post(post['id'], post['title'], post['content'], post['author_name'])
            self.posts.append(post_obj)

    def create_post(self, title, content, user):
        print(len(self.posts))
        new_post = {
            'id': len(self.posts) + 1,
            'title': title,
            'content': content,
            'author_id': user.id,
            'author_name': user.first_name + " " + user.last_name,
            'comments': []
        }
        insert_info(FORUM_FILE_PATH, new_post)
        self.posts.append(Post(new_post['id'], new_post['title'], new_post['content'], new_post['author_name']))
        print("Post created")

