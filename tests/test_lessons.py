import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.content import Content
from app.lessons import Lessons  
from database.database_management import *
from app.empoweru_constants import *

import pytest

@pytest.fixture
def sample_content_data():
    return [
        {
            "id": 1,
            "title": "Working with Textual Data",
            "type": "video",
            "content": "database/videos/testing.mp4"
        },
        {
            "id": 2,
            "title": "Integers and Floats(1)",
            "type": "text",
            "content": ("Integers are whole numbers that have no decimal point. They can be positive, negative, or zero. Integers are great for counting things, like the number of items in a list or a person's age. While Floats are numbers that have a decimal point. They can represent fractional or decimal values, such as measurements or monetary amounts. Floats are useful when you need precision in calculations, like calculating distances or working with currency.")
        }
    ]

@pytest.fixture
def sample_lesson(sample_content_data):
    return Lessons(
        id=1,
        title="Sample Lesson",
        lesson_type="text",
        content_list_data=sample_content_data
    )

#Test initializing content list
def test_init_content_list(sample_lesson):
    content_list = sample_lesson.get_content_list()
    assert len(content_list) == 2
    assert content_list[0].title == "Working with Textual Data"
    assert content_list[0].type == "video"
    assert content_list[0].content == "database/videos/testing.mp4"
    assert content_list[1].title == "Integers and Floats(1)"
    assert content_list[1].type == "text"
    assert content_list[1].content == ("Integers are whole numbers that have no decimal point. They can be positive, negative, or zero. Integers are great for counting things, like the number of items in a list or a person's age. While Floats are numbers that have a decimal point. They can represent fractional or decimal values, such as measurements or monetary amounts. Floats are useful when you need precision in calculations, like calculating distances or working with currency.")

#Test adding text content
def test_add_text_content(sample_lesson):
    sample_lesson.add_text("Lists, Tuples and Sets(1)")
    content_list = sample_lesson.get_content_list()
    assert len(content_list) == 3
    assert content_list[2].content == "Lists, Tuples and Sets(1)"
    assert content_list[2].type == "text"  

#Test adding video content
def test_add_video_content(sample_lesson):
    sample_lesson.add_video("/new/path/to/video.mp4")
    content_list = sample_lesson.get_content_list()
    assert len(content_list) == 3
    assert content_list[2].content == "/new/path/to/video.mp4"
    assert content_list[2].type == "video" 