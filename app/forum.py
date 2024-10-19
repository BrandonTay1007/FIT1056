import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database_management import *
from empoweru_constants import *

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

