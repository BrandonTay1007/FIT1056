import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from empoweru_constants import *
from database.database_management import *
from app.comment import Comment
class Post:
    def __init__(self, id, title, content, author):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.comments = []
        self.init_comments()
    
    def init_comments(self):
        posts_data = get_info_by_id(FORUM_FILE_PATH, 'id', self.id)
        comments = posts_data['comments']
        for comment in comments:
            comment_obj = Comment(comment['id'], comment['content'], comment['author_name'])
            self.comments.append(comment_obj)

    def add_comment(self, comment):
        self.comments.append(comment)
        update_info_by_id(FORUM_FILE_PATH, 'id', self.id, {'comments': self.comments})
        