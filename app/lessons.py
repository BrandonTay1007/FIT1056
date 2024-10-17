import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.content import Content
from interface.lessons_list import LessonsList
from database.database_management import *
from empoweru_constants import *

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

    def init_lessons_course_by_id(id):
        content_list = []
        lesson = get_info_by_id(LESSONS_FILE_PATH, id)

        for content in lesson["content_list"]:
            content_list.append(Content(content["id"], content["title"], content["type"], content["content"]))  

        return content_list



# if __name__ == "__main__":
#     lesson = Lessons(1, "Lesson 1", "lectures")
#     lesson.initalize_content()
#     print(lesson.get_content_list())