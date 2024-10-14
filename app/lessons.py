import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.content import Content
from database.database_management import *
from empoweru_constants import LESSONS_FILE_PATH

class Lessons:

    def __init__(self, id, title, lesson_type, content_list):
        self.id = id
        self.title = title
        self.lesson_type = lesson_type
        self.content_list = content_list

    def add_text(self, text):
        text_content = Content(self.id, self.title, "text", text)
        self.content_list.append(text_content)

    def add_video(self, video_path):
        video_content = Content(self.id, self.title, "video", video_path)
        self.content_list.append(video_content)
    
    def get_content_list(self):
        return self.content_list

# if __name__ == "__main__":
#     lesson = Lessons(1, "Lesson 1", "lectures")
#     lesson.initalize_content()
#     print(lesson.get_content_list())