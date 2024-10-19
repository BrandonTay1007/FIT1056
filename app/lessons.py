from app.content import Content
from database import *
from app.empoweru_constants import *

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

    @staticmethod
    def list_lessons_by_course():
        courses = extract_file_info(COURSES_FILE_PATH)
        lessons = extract_file_info(LESSONS_FILE_PATH)
        
        lessons_by_course = {}
        
        for course in courses:
            course_id = course['id']
            course_name = course['title']  # Changed from 'name' to 'title' based on your courses.json structure
            lessons_by_course[course_name] = []
            
            for lesson in lessons:
                if lesson['course_id'] == course_id:
                    lessons_by_course[course_name].append({
                        'id': lesson['id'],
                        'title': lesson['title'],
                        'lesson_type': lesson['lesson_type']
                    })
        
        return lessons_by_course

    @staticmethod
    def update_lesson(lesson_id, new_data):
        return update_info_by_id(LESSONS_FILE_PATH, 'id', lesson_id, new_data)

    @staticmethod
    def add_new_lesson(lesson_data):
        return insert_info(LESSONS_FILE_PATH, lesson_data)

    @staticmethod
    def delete_lesson(lesson_id):
        return remove_by_id(LESSONS_FILE_PATH, lesson_id)

    @staticmethod
    def get_lesson_by_id(lesson_id):
        lessons = extract_file_info(LESSONS_FILE_PATH)
        for lesson in lessons:
            if lesson['id'] == lesson_id:
                return lesson
        return None

    @staticmethod
    def get_course_id_by_name(course_name):
        courses = extract_file_info(COURSES_FILE_PATH)
        for course in courses:
            if course['title'] == course_name:
                return course['id']
        return None
