import os
import sys
import pytest
from unittest.mock import patch, MagicMock

# Construct the absolute path to the 'app' directory
app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../app'))
sys.path.append(app_path)

from app.forum import Forum
from app.posts import Post

# Mock constants
FORUM_FILE_PATH = "mock_forum_file_path"

# Mock data
mock_post_data = [
    {'id': 1, 'title': 'Post 1', 'content': 'Content 1', 'author_name': 'Author 1'},
    {'id': 2, 'title': 'Post 2', 'content': 'Content 2', 'author_name': 'Author 2'}
]

# Mock functions
def mock_extract_file_info(file_path):
    if file_path == FORUM_FILE_PATH:
        return mock_post_data
    return []

def mock_insert_info(file_path, data):
    pass

# Test cases
@patch('forum.extract_file_info', side_effect=mock_extract_file_info)
def test_init_posts(mock_extract):
    forum = Forum()
    assert len(forum.get_posts()) == 2  # Adjusted to match mock data
    assert forum.get_posts()[0].title == 'Post 1'
    assert forum.get_posts()[1].title == 'Post 2'

@patch('forum.insert_info', side_effect=mock_insert_info)
@patch('forum.extract_file_info', side_effect=mock_extract_file_info)
def test_create_post(mock_extract, mock_insert):
    forum = Forum()
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.first_name = "John"
    mock_user.last_name = "Doe"
    
    forum.create_post("New Post", "New Content", mock_user)
    
    assert len(forum.get_posts()) == 3  # Adjusted to account for initial mock data
    assert forum.get_posts()[-1].title == "New Post"
    assert forum.get_posts()[-1].content == "New Content"
    assert forum.get_posts()[-1].author_name == "John Doe"
    mock_insert.assert_called_once()

@patch('forum.extract_file_info', side_effect=mock_extract_file_info)
def test_add_post(mock_extract):
    forum = Forum()
    new_post = Post(3, "Another Post", "Another Content", "Another Author")
    forum.add_post(new_post)
    
    assert len(forum.get_posts()) == 3  # Adjusted to account for initial mock data
    assert forum.get_posts()[-1].title == "Another Post"
    assert forum.get_posts()[-1].content == "Another Content"
    assert forum.get_posts()[-1].author_name == "Another Author"
