import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.empoweru_constants import *
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
        # Assuming 'comment' is a dictionary with keys: 'content', 'author_id', 'author_name'
        new_comment = {
            'id': len(self.comments) + 1,
            'content': comment['content'],
            'author_id': comment['author_id'],
            'author_name': comment['author_name']
        }
        
        # Add to the local comments list
        self.comments.append(Comment(new_comment['id'], new_comment['content'], new_comment['author_name']))
        
        # Get the current post data
        post_data = get_info_by_id(FORUM_FILE_PATH, 'id', self.id)
        
        # Add the new comment to the post's comments
        post_data['comments'].append(new_comment)
        
        # Update the forum.json file
        update_info_by_id(FORUM_FILE_PATH, 'id', self.id, {'comments': post_data['comments']})
        
        print(f"Comment added: {new_comment}")
