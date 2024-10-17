import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.content import Content
from database.database_management import *
from empoweru_constants import *

class Lessons:

    def __init__(self, id, title, lesson_type, content_list_data):
        self.id = id
        self.title = title
        self.lesson_type = lesson_type
        self.content_list_data = content_list_data
        self.content_list = self.init_content_list()
    def __str__(self):
        return f"Lesson(id={self.id}, title={self.title}, lesson_type={self.lesson_type})"

    def add_text(self, text):
        text_content = Content(self.id, self.title, "text", text)
        self.content_list.append(text_content)


    def add_video(self, video_path):
        video_content = Content(self.id, self.title, "video", video_path)
        self.content_list.append(video_content)
        
    def get_content_list(self):
        return self.content_list

    def init_content_list(self):
        content_list = []
        for content in self.content_list_data:
            content_list.append(Content(content["id"], content["title"], content["type"], content["content"]))  

        return content_list



# if __name__ == "__main__":
#     lesson = Lessons(1, "Lesson 1", "lectures")
#     lesson.initalize_content()
#     print(lesson.get_content_list())